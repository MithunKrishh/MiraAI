from app.services.intent_service import detect_intent

def parse_tasks(text: str):
    # Split using simple keywords
    separators = [" and ", ",", " then "]

    tasks = [text]

    for sep in separators:
        if sep in text.lower():
            tasks = text.lower().split(sep)
            break

    parsed_intents = []

    for task in tasks:
        intent = detect_intent(task.strip())
        parsed_intents.append({
            "intent": intent,
            "text": task.strip()
        })

    return parsed_intents