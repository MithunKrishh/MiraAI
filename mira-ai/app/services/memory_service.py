import json
import os
from datetime import datetime

MEMORY_FILE = "data/memory.json"

def save_to_memory(task: str, result: str):
    try:
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, "r") as file:
            data = json.load(file)
    except Exception:
        data = []

    entry = {
        "task": task,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }

    data.append(entry)

    try:
        with open(MEMORY_FILE, "w") as file:
            json.dump(data, file, indent=2)
    except Exception:
        # Avoid crashing API calls if disk write fails.
        return


def get_last_entry():
    try:
        with open(MEMORY_FILE, "r") as file:
            data = json.load(file)
            if not data:
                return "No memory found."
            return data[-1]
    except Exception:
        return "Memory not initialized."