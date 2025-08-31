from transformers import pipeline

s_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment",
    device=0  # GPU kullanımı
)

labels = ['NEGATIVE', 'NEUTRAL', 'POSITIVE']

def analyze_sentiment(text: str) -> dict:
    raw_result = s_model(text)[0]
    label_idx = int(raw_result['label'].replace("LABEL_", ""))
    return {
        "label": labels[label_idx],
        "score": raw_result['score']
    }