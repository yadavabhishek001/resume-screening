import streamlit as st
from utils import extract_text_from_pdf, clean_text

st.title("AI Resume Screening System")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)", 
    type=["pdf"], 
    accept_multiple_files=True
)

if job_desc:
    job_desc = clean_text(job_desc)
    st.write("Job Description:", job_desc[:200])

if uploaded_files:
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        text = clean_text(text)

        st.write("Resume:", file.name)
        st.write("DEBUG:", text)
