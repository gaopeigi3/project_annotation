import json
from pathlib import Path

import yaml
from fastapi.testclient import TestClient

import api.main as api


def test_health():
    assert TestClient(api.app).get("/health").json() == {"status": "ok"}


def test_analysis_lifecycle(tmp_path, monkeypatch):
    runs_dir = tmp_path / "runs"
    monkeypatch.setattr(api, "RUNS_DIR", runs_dir)

    def fake_workflow(run_id: str, config_path: Path) -> None:
        run_dir = runs_dir / run_id
        result = run_dir / "results" / "demo" / "annotated.h5ad"
        result.parent.mkdir(parents=True)
        result.touch()
        api.write_status(run_dir, "completed")

    monkeypatch.setattr(api, "run_workflow", fake_workflow)
    client = TestClient(api.app)

    response = client.post(
        "/analysis",
        json={
            "cohort": "demo",
            "n_hvg": 1000,
            "n_neighbors": 10,
            "resolution": 1.0,
        },
    )
    assert response.status_code == 202
    run_id = response.json()["run_id"]

    config = yaml.safe_load((runs_dir / run_id / "config.yaml").read_text())
    assert config["cohort"]["name"] == "demo"
    assert config["paths"]["results_root"] == str(runs_dir / run_id / "results")
    assert config["paths"]["logs_root"] == str(runs_dir / run_id / "logs")

    assert client.get(f"/analysis/{run_id}").json()["status"] == "completed"
    results = client.get(f"/analysis/{run_id}/results")
    assert results.status_code == 200
    assert results.json()["files"] == ["results/demo/annotated.h5ad"]


def test_missing_run_returns_404(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "RUNS_DIR", tmp_path / "runs")
    response = TestClient(api.app).get("/analysis/missing")
    assert response.status_code == 404
