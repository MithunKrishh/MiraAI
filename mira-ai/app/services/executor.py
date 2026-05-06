from app.services.summarizer import summarize_text
from app.services.memory_service import save_to_memory, get_last_entry

def execute_task(intent: str, text: str) -> str:
    if intent == "summarize":
        result = summarize_text(text)
        save_to_memory(text, result)
        return result

    elif intent == "save":
        save_to_memory(text, text)
        return "Saved successfully."

    elif intent == "retrieve":
        return str(get_last_entry())

    return "Sorry, I don't understand this task yet."