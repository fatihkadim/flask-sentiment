DEFAULT_LANGUAGE='en'

from .preprocessing import clean_text
from .model import analyze_sentiment
from .utils import format_result

__all__ = ["clean_text", "analyze_sentiment", "format_result"]