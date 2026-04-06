import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_similarity

st.title("AI Resume Screening System")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)", 
    type=["pdf"], 
    accept_multiple_files=True
)

if uploaded_files and job_desc:
    job_desc_clean = clean_text(job_desc)

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        text_clean = clean_text(text)

        score = calculate_similarity(job_desc_clean, text_clean)

        st.write("Resume:", file.name)
        st.write("Match Score:", round(score * 100, 2), "%")
