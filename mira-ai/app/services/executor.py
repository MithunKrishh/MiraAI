from app.services.summarizer import summarize_text
from app.services.memory_service import save_to_memory, get_last_entry

def execute_task(intent: str, text: str) -> str:
    if not intent or not isinstance(intent, str):
        intent = "unknown"
    if not text or not isinstance(text, str):
        return "Invalid task text."

    if intent == "summarize":
        try:
            result = summarize_text(text)
            save_to_memory(text, result)
            return result
        except Exception:
            return "Failed to summarize."

    elif intent == "save":
        try:
            save_to_memory(text, text)
            return "Saved successfully."
        except Exception:
            return "Failed to save."

    elif intent == "retrieve":
        try:
            return str(get_last_entry())
        except Exception:
            return "Failed to retrieve memory."

    return "Sorry, I don't understand this task yet."