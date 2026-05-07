import app.routes.task_routes as task_routes


def test_root_health(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.json()


def test_task_returns_results(client, monkeypatch):
    # Avoid running heavy summarizer/model in tests.
    monkeypatch.setattr(task_routes, "execute_task", lambda intent, text: f"ok:{intent}")

    res = client.post("/task/", json={"input": "summarize this and save it"})

    assert res.status_code == 200
    body = res.json()
    assert body["message"]
    assert body["input"]
    assert len(body["tasks"]) == 2
    assert body["tasks"][0]["intent"] == "summarize"
    assert body["tasks"][0]["result"].startswith("ok:")


def test_task_empty_input_422(client):
    res = client.post("/task/", json={"input": "   "})
    assert res.status_code == 422


def test_task_parse_failure_returns_400(client, monkeypatch):
    monkeypatch.setattr(task_routes, "parse_tasks", lambda _text: (_ for _ in ()).throw(ValueError("bad")))

    res = client.post("/task/", json={"input": "retrieve"})
    assert res.status_code == 400
    assert res.json()["detail"] == "Failed to parse tasks from input."
