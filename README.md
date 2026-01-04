# Text Analyzer

A Flask-based web application designed to provide detailed text analysis and metrics.

## Description
This project allows users to input blocks of text and receive immediate feedback on word counts, character counts, and frequency analysis. It features a flexible text-processing pipeline to handle normalization, case sensitivity, and stop-word filtering.

### Goals
- [x] Basic text input interface and word count.
- [x] Apostrophe preservation in normalization.
- [ ] Implement a modular **Pipeline Pattern** for text processing.
- [ ] Add user toggles for **Case Sensitivity** and **Stop Words**.
- [ ] Display advanced metrics: Unique words and Most Frequent words.
- [ ] Dictionary check for "Words not in dictionary" (Future goal).

## Technical Implementation Steps
To achieve the remaining goals, the following steps will be taken:
1. **Refactor Processing**: Transition from static functions to a `TextPipeline` class or higher-order function.
2. **UI Update**: Modify `templates/post.html` to include toggle switches for analysis options.
3. **Backend Integration**: Update `app.py` to capture form toggles and configure the pipeline dynamically.
4. **Data Enrichment**: Integrate a standard stop-word list (or NLTK) for better filtering accuracy.

## Getting Started

### Dependencies
- Python 3.8+
- Flask
- (Optional) NLTK for advanced language processing

### Installing
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Executing program
1. Run the Flask development server:
   ```bash
   python app.py
   ```
2. Navigate to `http://127.0.0.1:5000` in your browser.

## Acknowledgments
* Regex patterns for text normalization.
* Flask documentation for web routing.

