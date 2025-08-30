def format_result(result: dict) -> str:
    return f"{result['label']} (Confidence: {round(result['score'], 3)})"
