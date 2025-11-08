import streamlit as st
from pdf_enhancer import enhance_pdf
import io

st.set_page_config(page_title="PDF → 최대 화질 PDF", layout="wide")
st.title("📄 PDF → 최대 화질 PDF 변환기 (CPU 전용)")

uploaded_pdf = st.file_uploader("PDF 파일 업로드", type=["pdf"])

if uploaded_pdf:
    st.write("PDF 업로드 완료")
    if st.button("최대 화질 PDF 변환"):
        with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
            highres_pdf = enhance_pdf(uploaded_pdf)
        st.success("PDF 변환 완료 ✅")
        st.download_button(
            "PDF 다운로드",
            data=highres_pdf,
            file_name="highres_converted.pdf"
        )
