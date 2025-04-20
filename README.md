# ResumeParser
A lightweight Python command-line tool for extracting text and named entities from PDF resumes, outputting structured JSON data for easy integration with HR systems, analytics pipelines, or custom applications.

## Features

PDF Text Extraction: Parses multi-page PDFs using PyPDF2.

Named Entity Recognition: Leverages spaCy en_core_web_sm to identify entities (PERSON, ORG, GPE, DATE, etc.).

Auto Model Installation: Downloads the spaCy model if not present.

Customizable Output: Specify the output JSON filename and path.

Cross-Platform: Runs on Windows, macOS, and Linux.


