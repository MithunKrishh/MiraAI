from app.services.summarizer import summarize_text

def execute_task(intent: str, text: str) -> str:
    if intent == "summarize":
        return summarize_text(text)

    elif intent == "save":
        return f"Data will be saved: {text}"
    
    elif intent == "retrieve":
        return "Retrieving stored data..."
    
    return "Sorry, I don't understand this task yet."