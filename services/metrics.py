# Output File for the final metrics
from collections import Counter

def get_word_count(words):
    """Returns total number of words."""
    return len(words)

def get_unique_word_count(words):
    """Returns number of unique words."""
    return len(set(words))

def get_most_frequent_words(words, n=10):
    """Returns the n most frequent words."""
    return Counter(words).most_common(n)

def get_character_count(text):
    """Returns total number of characters in raw text."""
    return len(text)
