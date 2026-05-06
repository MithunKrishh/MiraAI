import json
from datetime import datetime

MEMORY_FILE = "data/memory.json"

def save_to_memory(task: str, result: str):
    try:
        with open(MEMORY_FILE, "r") as file:
            data = json.load(file)
    except:
        data = []

    entry = {
        "task": task,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }

    data.append(entry)

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=2)


def get_last_entry():
    try:
        with open(MEMORY_FILE, "r") as file:
            data = json.load(file)
            if not data:
                return "No memory found."
            return data[-1]
    except:
        return "Memory not initialized."