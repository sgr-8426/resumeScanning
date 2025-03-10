import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_pdf_content(uploaded_pdf):
    reader = PdfReader(uploaded_pdf)
    return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

def evaluate_resumes(job_text, resume_contents):
    combined_texts = [job_text] + resume_contents
    tfidf_model = TfidfVectorizer().fit_transform(combined_texts)
    similarity_scores = cosine_similarity(tfidf_model[0:1], tfidf_model[1:]).flatten()
    return similarity_scores

# Streamlit UI Design
st.set_page_config(page_title="Resume Ranker AI", layout="wide")
st.markdown("""
    <style>
        .title {text-align: center; font-size: 30px; font-weight: bold; color: #2C3E50;}
        .subtitle {text-align: center; font-size: 18px; color: #7F8C8D;}
        .stApp {background-color: #ECF0F1;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='title'>🤖 Resume Ranking System</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload resumes and get ranked based on job relevance!</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📌 Job Description")
    job_text = st.text_area("Paste the job description here", height=200)
    st.subheader("📂 Upload Resumes")
    uploaded_resumes = st.file_uploader("Select PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_resumes and job_text:
    with col2:
        st.subheader("🏆 Ranking Results")
        resume_texts = [extract_pdf_content(resume) for resume in uploaded_resumes]
        scores = evaluate_resumes(job_text, resume_texts)
        ranking = pd.DataFrame({
            "Candidate": [resume.name for resume in uploaded_resumes],
            "Relevance Score (%)": (scores * 100).round(2)
        }).sort_values(by="Relevance Score (%)", ascending=False)
        st.dataframe(ranking, use_container_width=True)
        st.balloons()
        st.success("Ranking completed! Check the results above.")
