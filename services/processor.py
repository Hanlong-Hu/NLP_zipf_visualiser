# Runs the pipeline of the text analysis
from services.steps import tokenize_step

def run_pipeline(text, steps):
    """
    Orchestrates the text processing pipeline.
    :param text: Raw input string
    :param steps: List of functions to apply to the tokens
    :return: List of processed tokens
    """
    # Start with tokenization
    data = tokenize_step(text)
    
    # Apply each step in the pipeline
    for step in steps:
        data = step(data)
        
    return data
