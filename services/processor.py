# Runs the pipeline of the text analysis

def run_pipeline(text, steps):
    """
    Orchestrates the text processing pipeline and tracks intermediate states.
    :param text: Raw input string
    :param steps: List of tuples (name, function)
    :return: Tuple of (final_data, snapshots)
    """
    data = text
    snapshots = {}
    
    # Apply each step in the pipeline
    for name, step_func in steps:
        data = step_func(data)
        if name:
            snapshots[name] = data
            
    return data, snapshots
