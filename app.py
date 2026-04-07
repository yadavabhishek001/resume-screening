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

    results = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        text_clean = clean_text(text)

        score = calculate_similarity(job_desc_clean, text_clean)

        results.append((file.name, score))

    # Sort by score (highest first)
    results = sorted(results, key=lambda x: x[1], reverse=True)

    st.subheader("Ranked Resumes")

    for i, (name, score) in enumerate(results, start=1):
        st.write(f"{i}. {name} - {round(score * 100, 2)}%")
