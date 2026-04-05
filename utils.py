import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text
