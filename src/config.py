from pathlib import Path

class config:
    """Configuration class for the application."""

    #Model settings
    SPACY_MODEL = "en_core_web_md"

    #File path
    BASE_DIR = Path(__file__).parent.parent
    OUT_PUT = BASE_DIR / "output"

    # Analysis settings
    DEFAULT_NUM_KEYWORDS = 5
    DEFAULT_NUM_SUMMARY_SENTENCES = 3
    
    # Logging settings
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_LEVEL = "INFO"
