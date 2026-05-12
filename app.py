import streamlit as st
from utils import (
    extract_text_from_pdf,
    clean_text,
    calculate_similarity,
    get_matched_skills,
    get_missing_skills
)

st.set_page_config(page_title="AI Resume Screening System")

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

    # Process resumes
    for file in uploaded_files:

        text = extract_text_from_pdf(file)
        text_clean = clean_text(text)

        score = calculate_similarity(job_desc_clean, text_clean)

        matched = get_matched_skills(job_desc_clean, text_clean)

        missing = get_missing_skills(job_desc_clean, text_clean)

        results.append({
            "name": file.name,
            "score": score,
            "matched": matched,
            "missing": missing
        })

    # Sort resumes by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.subheader("Ranked Resumes")

    # Display ranked resumes
    for i, result in enumerate(results, start=1):

        st.markdown("---")

        st.subheader(
            f"{i}. {result['name']} - {round(result['score'] * 100, 2)}%"
        )

        st.success(
            f"Matched Skills: {', '.join(result['matched'][:5])}"
        )

        st.error(
            f"Missing Skills: {', '.join(result['missing'][:5])}"
        )
