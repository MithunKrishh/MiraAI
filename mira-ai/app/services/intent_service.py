def detect_intent(text: str) -> str:
    text = text.lower()

    if "summarize" in text:
        return "summarize"
    elif "save" in text:
        return "save"
    elif "retrieve" in text or "show" in text:
        return "retrieve"
    
    return "unknown"