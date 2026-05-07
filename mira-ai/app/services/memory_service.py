from datetime import datetime

from app.core.db import get_memory_collection

def save_to_memory(task: str, result: str):
    """Store a task execution result in MongoDB.

    If MongoDB is unavailable, we swallow the error to prevent API crashes.
    """
    entry = {"task": task, "result": result, "timestamp": datetime.now().isoformat()}

    try:
        collection = get_memory_collection()
        collection.insert_one(entry)
    except Exception:
        return


def get_last_entry():
    """Return the most recent memory entry.

    Returns strings for backwards compatibility with older behavior.
    """
    try:
        collection = get_memory_collection()
        doc = collection.find_one(sort=[("timestamp", -1)])
        if not doc:
            return "No memory found."
        doc.pop("_id", None)
        return doc
    except Exception:
        return "Memory not initialized."