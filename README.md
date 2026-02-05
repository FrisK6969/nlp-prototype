# NLP Information Extraction Prototype

A slim and simple Python-based prototype demonstrating Named Entity Recognition (NER) to extract structured information from unstructured text data.

## Overview
This project includes:
- **Text Processing:** Basic preprocessing and tokenization of raw text input.
- **Information Extraction:** Named Entity Recognition to identify entities such as *Persons* and *Organizations* using a pretrained spaCy language pipeline.
- **Interactive UI:** A minimal Streamlit-based web interface for real-time text analysis and visualization of extracted entities.

The project is intended as an exploratory prototype to demonstrate core concepts of **NLP pipelines** and **information extraction**.

## Language Specification
> **Note:** The current version is configured for **German** text data.
> - The **User Interface (UI)** is written in German.
> - The NLP pipeline uses the spaCy model `de_core_news_lg`, optimized for German syntax and named entities.
> - For English support, the model pipeline can be easily swapped to `en_core_web_lg`.

## Installation & Setup
To run this prototype locally, ensure you have Python 3.12+ installed.

1. **Clone the repository:**
   ```
   git clone https://github.com/FrisK6969/nlp-prototype.git
   cd prototype
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download the German Language Model:**
   ```
   python -m spacy download de_core_news_lg
   ```

4. **Launch the Application:**
   ```
   streamlit run nlp_prototype.py
   ```
