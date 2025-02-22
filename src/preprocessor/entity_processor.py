from .base_processor import BaseProcessor
from spacy.tokens import Doc
from typing import List, Dict

class EntityProcessor(BaseProcessor):
    """Processor for named entity recognition."""
    
    def process(self, doc: Doc) -> List[Dict]:
        """Extract named entities from text."""
        return [{
            'text': ent.text,                   #This will give the text of the entity
            'label': ent.label_,                #This will give the label of the entity
            'start': ent.start_char,            #This will give the start character of the entity
            'end': ent.end_char                 #This will give the end character of the entity
        } for ent in doc.ents]