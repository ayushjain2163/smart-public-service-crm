from transformers import pipeline

# Sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")

# Text generation model (used for summarization)
summarizer = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

CATEGORY_KEYWORDS = {
    "Road Infrastructure": ["road", "pothole", "street"],
    "Water Supply": ["water", "pipeline", "tap"],
    "Electricity": ["electricity", "power", "light"],
    "Sanitation": ["garbage", "waste", "sewer"],
    "Healthcare": ["hospital", "doctor"]
}


def detect_category(text):

    text = text.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "General"


def detect_sentiment(text):

    result = sentiment_pipeline(text)[0]

    if result["label"] == "POSITIVE":
        return "Positive"

    if result["label"] == "NEGATIVE":
        return "Negative"

    return "Neutral"


def summarize_text(text):

    prompt = f"""
Summarize the following government report in 3-4 sentences:

{text}
"""

    result = summarizer(
        prompt,
        max_new_tokens=80
    )

    return result[0]["generated_text"]
