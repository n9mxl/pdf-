import streamlit as st
from pdf_generator import enhance_and_create_pdf

st.set_page_config(page_title="이미지 → 고화질 PDF 변환기", layout="wide")
st.title("📚 이미지 → 고화질 PDF 변환기")

container = st.container()
with container:
    uploaded_files = st.file_uploader(
        "페이지 이미지 선택", 
        type=["png","jpg","jpeg"], 
        accept_multiple_files=True
    )

if uploaded_files:
    if st.button("PDF 변환"):
        with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
            pdf_bytes = enhance_and_create_pdf(uploaded_files)
        st.success("PDF 변환 완료 ✅")
        st.download_button("PDF 다운로드", data=pdf_bytes, file_name="교과서.pdf")
