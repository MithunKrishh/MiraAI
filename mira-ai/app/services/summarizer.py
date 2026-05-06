from transformers import pipeline

# Load once (important)
summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    if len(text.split()) < 10:
        return "Text too short to summarize."

    result = summarizer(
        text,
        max_length=50,
        min_length=20,
        do_sample=False
    )

    return result[0]['summary_text']