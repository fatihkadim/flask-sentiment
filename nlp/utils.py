def format_result(result: dict) -> dict:
    return {
        "label": result["label"],
        "score": round(result["score"], 3)
    }
