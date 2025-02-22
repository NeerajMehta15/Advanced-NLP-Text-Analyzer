from .base_processor import BaseProcessor
from spacy.tokens import Doc

class SummaryProcessor(BaseProcessor):
    """Processor for text summarization."""
    
    def process(self, doc: Doc, num_sentences: int) -> str:
        """Generate text summary."""
        sentence_scores = self._score_sentences(doc)
        return self._generate_summary(doc, sentence_scores, num_sentences)
    
    def _score_sentences(self, doc: Doc) -> dict:
        """Score sentences based on various factors."""
        scores = {}
        
        for sent in doc.sents:
            score = 0
            score += len([ent for ent in sent.ents])
            
            for token in sent:
                if not token.is_stop and not token.is_punct:
                    score += token.prob
            
            scores[sent.text] = score / len(sent)
        
        return scores
    
    def _generate_summary(self, doc: Doc, 
                         sentence_scores: dict, 
                         num_sentences: int) -> str:
        """Generate summary from top-scored sentences."""
        summary_sentences = sorted(
            sentence_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:num_sentences]
        
        return ' '.join(sent for sent, _ in sorted(
            summary_sentences,
            key=lambda x: doc.text.find(x[0])
        ))