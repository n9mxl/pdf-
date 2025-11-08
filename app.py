import streamlit as st
from pdf_generator import enhance_and_create_pdf

st.set_page_config(page_title="이미지 → 최대 화질 PDF 변환기", layout="wide")
st.title("📚 이미지 → 최대 화질 PDF 변환기 (CPU 전용)")

# 세션 상태 초기화
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# 다중 파일 업로드
uploaded_files = st.file_uploader(
    "페이지 이미지 선택 (여러 개 선택 가능)", 
    type=["png","jpg","jpeg"], 
    accept_multiple_files=True
)

# 업로드된 파일을 세션 상태에 저장
if uploaded_files:
    st.session_state.uploaded_files = uploaded_files

# 업로드된 이미지 파일 목록 표시
if st.session_state.uploaded_files:
    st.write("업로드된 이미지:")
    for i, file in enumerate(st.session_state.uploaded_files, start=1):
        st.write(f"{i}. {file.name}")

# PDF 변환 버튼
if st.session_state.uploaded_files:
    if st.button("PDF 변환 (최대 화질)"):
        with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
            pdf_bytes = enhance_and_create_pdf(st.session_state.uploaded_files)
        st.success("PDF 변환 완료 ✅")
        st.download_button("PDF 다운로드", data=pdf_bytes, file_name="교과서_highres.pdf")
