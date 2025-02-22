import spacy
from typing import Dict
import json
from pathlib import Path

from .config import Config
from .utils.logging_utils import setup_logging
from .processors.keyword_processor import KeywordProcessor
from .processors.entity_processor import EntityProcessor
from .processors.summary_processor import SummaryProcessor

class TextAnalyzer:
    """Main class for text analysis."""
    
    def __init__(self):
        """Initialize the analyzer with necessary processors."""
        self.logger = setup_logging()
        
        try:
            self.nlp = spacy.load(Config.SPACY_MODEL)
            
            # Initialize processors
            self.keyword_processor = KeywordProcessor(self.nlp)
            self.entity_processor = EntityProcessor(self.nlp)
            self.summary_processor = SummaryProcessor(self.nlp)
            
        except OSError as e:
            self.logger.error(
                f"Model '{Config.SPACY_MODEL}' not found. "
                f"Please install it using: python -m spacy download {Config.SPACY_MODEL}"
            )
            raise

    def analyze_text(self, text: str, 
                    num_keywords: int = Config.DEFAULT_NUM_KEYWORDS,
                    num_summary_sentences: int = Config.DEFAULT_NUM_SUMMARY_SENTENCES) -> Dict:
        """Perform comprehensive text analysis."""
        try:
            doc = self.nlp(text)
            
            analysis = {
                'summary': self.summary_processor.process(
                    doc, num_summary_sentences
                ),
                'keywords': self.keyword_processor.process(
                    doc, num_keywords
                ),
                'named_entities': self.entity_processor.process(doc),
                'statistics': self._calculate_statistics(doc)
            }
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Text analysis failed: {str(e)}")
            raise

    def _calculate_statistics(self, doc: Doc) -> Dict:
        """Calculate text statistics."""
        return {
            'num_sentences': len(list(doc.sents)),
            'num_tokens': len(doc),
            'num_entities': len(doc.ents),
            'avg_sentence_length': sum(len(sent) 
                                    for sent in doc.sents) / len(list(doc.sents))
        }

    def save_analysis(self, analysis: Dict, filepath: str):
        """Save analysis results to JSON file."""
        output_path = Path(filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with output_path.open('w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
