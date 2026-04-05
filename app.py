import streamlit as st
from utils import extract_text_from_pdf

st.title("AI Resume Screening System")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)", 
    type=["pdf"], 
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        st.write("Resume:", file.name)
        st.write(text[:500])  # show first 500 chars
