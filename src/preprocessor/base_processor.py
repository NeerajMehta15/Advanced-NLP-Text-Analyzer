from abc import ABC, abstractmethod
import spacy
from spacy.tokens import Doc

class BaseProcessor(ABC):
    """Base class for text processors."""
    
    def __init__(self, nlp):
        self.nlp = nlp
    
    @abstractmethod
    def process(self, *args, **kwargs):
        """Process the input data."""
        pass