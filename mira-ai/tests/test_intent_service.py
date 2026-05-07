from app.services.intent_service import detect_intent


def test_detect_intent_summarize():
    assert detect_intent("please summarize this") == "summarize"


def test_detect_intent_save():
    assert detect_intent("save this note") == "save"


def test_detect_intent_retrieve_show():
    assert detect_intent("show last") == "retrieve"


def test_detect_intent_unknown():
    assert detect_intent("do something else") == "unknown"


def test_detect_intent_phrase_make_shorter():
    assert detect_intent("make this shorter") == "summarize"


def test_detect_intent_phrase_show_my_tasks():
    assert detect_intent("show my tasks") == "retrieve"
