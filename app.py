import streamlit as st
from pdf_enhancer import enhance_pdf

st.set_page_config(page_title="PDF → 최대 화질 PDF", layout="wide")
st.title("📄 PDF → 최대 화질 PDF 변환기 (Poppler 불필요)")

# PDF 업로드
uploaded_pdf = st.file_uploader("PDF 파일 업로드", type=["pdf"])

# 변환 버튼
if uploaded_pdf and st.button("최대 화질 PDF 변환"):
    with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
        st.session_state['highres_pdf'] = enhance_pdf(uploaded_pdf)
    st.success("PDF 변환 완료 ✅")

# 다운로드 버튼 (DOM 오류 방지)
if 'highres_pdf' in st.session_state:
    st.download_button(
        "PDF 다운로드",
        data=st.session_state['highres_pdf'],
        file_name="highres_converted.pdf"
    )
