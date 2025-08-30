from transformers import pipeline

s_model = pipeline('sentiment-analysis')

def analyze_sentiment(text: str) -> dict:
    return s_model(text)[0]