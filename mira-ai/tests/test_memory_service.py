from datetime import datetime

import app.services.memory_service as memory_service


class FakeCollection:
    def __init__(self):
        self.docs = []

    def insert_one(self, doc):
        self.docs.append(doc)

    def find_one(self, sort=None):
        if not self.docs:
            return None
        # Memory service sorts by timestamp desc. We'll just emulate by max timestamp.
        return max(self.docs, key=lambda d: d.get("timestamp", ""))


def test_save_to_memory_inserts_document(monkeypatch):
    fake = FakeCollection()
    monkeypatch.setattr(memory_service, "get_memory_collection", lambda: fake)

    memory_service.save_to_memory("task1", "result1")

    assert len(fake.docs) == 1
    assert fake.docs[0]["task"] == "task1"
    assert fake.docs[0]["result"] == "result1"
    # basic sanity check
    datetime.fromisoformat(fake.docs[0]["timestamp"])


def test_get_last_entry_returns_latest(monkeypatch):
    fake = FakeCollection()
    monkeypatch.setattr(memory_service, "get_memory_collection", lambda: fake)

    fake.insert_one({"task": "t1", "result": "r1", "timestamp": "2020-01-01T00:00:00"})
    fake.insert_one({"task": "t2", "result": "r2", "timestamp": "2021-01-01T00:00:00"})

    last = memory_service.get_last_entry()
    assert last["task"] == "t2"
    assert last["result"] == "r2"


def test_memory_service_handles_db_down(monkeypatch):
    def _raise():
        raise RuntimeError("db down")

    monkeypatch.setattr(memory_service, "get_memory_collection", _raise)

    # should not raise
    memory_service.save_to_memory("t", "r")
    assert memory_service.get_last_entry() == "Memory not initialized."
