from app.services.parser import parse_tasks


def test_parse_tasks_splits_on_and():
    tasks = parse_tasks("summarize this and save it")
    assert len(tasks) == 2
    assert tasks[0]["intent"] == "summarize"
    assert tasks[1]["intent"] == "save"


def test_parse_tasks_splits_on_then():
    tasks = parse_tasks("retrieve then save")
    assert len(tasks) == 2
    assert tasks[0]["intent"] == "retrieve"
    assert tasks[1]["intent"] == "save"


def test_parse_tasks_no_split_returns_one_task():
    tasks = parse_tasks("retrieve")
    assert len(tasks) == 1
    assert tasks[0]["intent"] == "retrieve"
