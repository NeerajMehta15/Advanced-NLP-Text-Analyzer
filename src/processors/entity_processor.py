from .base_processor import BaseProcessor
from spacy.tokens import Doc
from typing import List, Dict

class EntityProcessor(BaseProcessor):
    """Processor for named entity recognition."""
    
    def process(self, doc: Doc) -> List[Dict]:
        """Extract named entities from text."""
        return [{
            'text': ent.text,
            'label': ent.label_,
            'start': ent.start_char,
            'end': ent.end_char
        } for ent in doc.ents]