import os
import spacy
import json
import webbrowser
from collections import defaultdict

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise ImportError("Please install PyPDF2: pip install PyPDF2")


class ResumeParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""

    def extract_text_from_pdf(self):
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"File not found: {self.pdf_path}")

        with open(self.pdf_path, 'rb') as file:
            reader = PdfReader(file)
            self.text = " ".join([page.extract_text() or "" for page in reader.pages])
        return self.text.strip()

    def extract_entities(self):
        nlp = self.load_spacy_model()
        doc = nlp(self.text)

        entities = defaultdict(list)
        for ent in doc.ents:
            entities[ent.label_].append(ent.text)

        return dict(entities)

    def load_spacy_model(self):
        try:
            return spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy model...")
            from spacy.cli import download
            download("en_core_web_sm")
            return spacy.load("en_core_web_sm")


if __name__ == "__main__":
    input_pdf = "path_to_resume"  # Update this path as needed
    output_json = "resume_entities.json"

    parser = ResumeParser(input_pdf)
    resume_text = parser.extract_text_from_pdf()
    extracted_data = parser.extract_entities()

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)

    print(f"Resume entities extracted and saved to: {output_json}")

    # 🔥Open the JSON file in the default editor or browser
    abs_path = os.path.abspath(output_json)
    webbrowser.open(f"file://{abs_path}")
