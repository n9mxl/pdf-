import streamlit as st
from pdf_generator import enhance_and_create_pdf

st.title("이미지 → 고화질 PDF 변환기")

uploaded_files = st.file_uploader(
    "페이지 이미지 선택", 
    type=["png","jpg","jpeg"], 
    accept_multiple_files=True
)

if st.button("PDF 변환"):
    if uploaded_files:
        pdf_bytes = enhance_and_create_pdf(uploaded_files)
        st.download_button("PDF 다운로드", data=pdf_bytes, file_name="교과서.pdf")
    else:
        st.warning("이미지를 먼저 업로드해주세요.")
