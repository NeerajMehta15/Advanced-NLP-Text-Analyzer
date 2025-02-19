from .base_processor import BaseProcessor
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Tuple


class KeywordProcessor(BaseProcessor):
    """Process text data into keywords."""

    def process(self, doc: Doc, num_keywords: int) -> List[Tuple[str, float]]:
        """Extract keywords using TF-IDF and spaCy's token attributes."""
        filtered_tokens = [token.lemma_ for token in doc if self._is__valid_token(token)]

        # Calculate TF-IDF scores
        return self._calculate_keyword_scores(filtered_tokens, num_keywords)
    

    def _is_valid_token(self, token: Token) -> bool:
        """Check if token is a valid keyword."""
        return (not token.is_stop and not token.is_punct and not token.is_space and token.pos_ in {'NOUN', 'PROPN', 'ADJ'})      
    

    def _calculate_keyword_scores(self, tokens: List[str], num_keywords: int) -> List[Tuple[str, float]]:
        """Calculate keyword scores using TF-IDF."""
        vectorizer = TfidfVectorizer(lowercase=True)
        tfidf_matrix = vectorizer.fit_transform([' '.join(tokens)])

        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]

        keyword_scores = list(zip(feature_names, scores))
        return sorted(keyword_scores, 
                     key=lambda x: x[1], 
                     reverse=True)[:num_keywords]