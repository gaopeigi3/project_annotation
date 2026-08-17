import json
from pathlib import Path
import subprocess
from uuid import uuid4

import yaml
from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel, Field

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = PROJECT_ROOT / "runs"
BASE_CONFIG_PATH = PROJECT_ROOT / "config/config.yaml"

app = FastAPI(title="scRNA Annotation API", version="0.1.0")


class AnalysisRequest(BaseModel):
    cohort: str = Field(min_length=1)
    n_hvg: int = Field(default=2000, gt=0)
    n_neighbors: int = Field(default=15, gt=0)
    resolution: float = Field(default=0.8, gt=0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def build_run_config(request: AnalysisRequest, run_dir: Path) -> dict:
    with BASE_CONFIG_PATH.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    config["cohort"]["name"] = request.cohort
    config["params"]["preprocess"]["n_hvg"] = request.n_hvg
    config["params"]["reduce"]["n_neighbors"] = request.n_neighbors
    config["params"]["reduce"]["resolution"] = request.resolution
    config["paths"]["results_root"] = str(run_dir / "results")
    config["paths"]["logs_root"] = str(run_dir / "logs")
    return config


def write_status(run_dir: Path, status: str) -> None:
    with (run_dir / "status.json").open("w", encoding="utf-8") as handle:
        json.dump({"status": status}, handle, indent=2)


def run_workflow(run_id: str, config_path: Path) -> None:
    run_dir = RUNS_DIR / run_id
    write_status(run_dir, "running")

    try:
        result = subprocess.run(
            [
                "snakemake",
                "--cores",
                "1",
                "--configfile",
                str(config_path),
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        with (run_dir / "snakemake.log").open("w", encoding="utf-8") as handle:
            handle.write(result.stdout)
            handle.write("\n--- STDERR ---\n")
            handle.write(result.stderr)
        write_status(run_dir, "completed" if result.returncode == 0 else "failed")
    except Exception as exc:
        write_status(run_dir, "failed")
        with (run_dir / "snakemake.log").open("w", encoding="utf-8") as handle:
            handle.write(f"Workflow execution error: {exc}\n")


def _load_status(run_id: str) -> tuple[Path, dict]:
    run_dir = RUNS_DIR / run_id
    status_path = run_dir / "status.json"
    if not status_path.exists():
        raise HTTPException(status_code=404, detail="Run not found")
    with status_path.open(encoding="utf-8") as handle:
        return run_dir, json.load(handle)


@app.get("/analysis/{run_id}")
def get_analysis_status(run_id: str) -> dict:
    _, status = _load_status(run_id)
    return {"run_id": run_id, **status}


@app.post("/analysis", status_code=202)
def analysis(
    request: AnalysisRequest,
    background_tasks: BackgroundTasks,
) -> dict[str, str]:
    run_id = str(uuid4())
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    config_path = run_dir / "config.yaml"
    run_config = build_run_config(request, run_dir)
    with config_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(run_config, handle, sort_keys=False)

    write_status(run_dir, "received")
    background_tasks.add_task(run_workflow, run_id, config_path)
    return {"run_id": run_id, "status": "received"}


@app.get("/analysis/{run_id}/results")
def get_analysis_results(run_id: str) -> dict:
    run_dir, status = _load_status(run_id)
    if status["status"] != "completed":
        raise HTTPException(
            status_code=409,
            detail=f"Run is not completed. Current status: {status['status']}",
        )

    results_dir = run_dir / "results"
    if not results_dir.exists():
        raise HTTPException(status_code=404, detail="Results not found")

    files = sorted(
        str(path.relative_to(run_dir))
        for path in results_dir.rglob("*")
        if path.is_file()
    )
    return {"run_id": run_id, "status": "completed", "files": files}
