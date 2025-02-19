import logging

from ..config import config

def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(format=config.LOG_FORMAT, level=config.LOG_LEVEL)
    return logging.getLogger(__name__)

