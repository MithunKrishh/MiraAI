from app.services.summarizer import summarize_text
from app.services.memory_service import save_to_memory, get_last_entry


def execute_single_task(intent: str, text: str):
    if intent == "summarize":
        return summarize_text(text)

    elif intent == "save":
        save_to_memory(text, text)
        return "Saved successfully."

    elif intent == "retrieve":
        return str(get_last_entry())

    return text


def execute_pipeline(tasks):
    current_output = None

    for task in tasks:
        intent = task["intent"]
        text = task["text"]

        # 🔥 Pass previous output if exists
        if current_output:
            text = current_output

        current_output = execute_single_task(intent, text)

    return current_output