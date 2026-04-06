import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

def calculate_similarity(job_desc, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_desc, resume_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]
