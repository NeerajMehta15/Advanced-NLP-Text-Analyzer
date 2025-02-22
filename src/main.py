from .analyzer import TextAnalyzer

def main():
    """Example usage of the TextAnalyzer."""
    # Sample text
    sample_text = """
    SpaCy is an open-source software library for advanced Natural Language Processing. 
    It is designed specifically for production use and helps build applications that process 
    large volumes of text. SpaCy can be used to build information extraction, natural language 
    understanding systems, and pre-processing text for deep learning.
    """
    
    # Initialize analyzer
    analyzer = TextAnalyzer()
    
    # Perform analysis
    results = analyzer.analyze_text(sample_text)
    
    # Save results
    analyzer.save_analysis(results, "analysis_results.json")
    
    return results

if __name__ == "__main__":
    main()