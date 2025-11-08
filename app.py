import streamlit as st
from pdf_generator import enhance_and_create_pdf
import zipfile
import io

st.set_page_config(page_title="ZIP → 최대 화질 PDF 변환기", layout="wide")
st.title("📚 ZIP 파일 → 최대 화질 PDF 변환기 (CPU 전용)")

# ZIP 파일 업로드
uploaded_zip = st.file_uploader("ZIP 파일 업로드 (이미지 포함, 40장 이상 가능)", type=["zip"])

if uploaded_zip:
    images = []
    with zipfile.ZipFile(uploaded_zip) as z:
        for file_name in z.namelist():
            if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                img_bytes = io.BytesIO(z.read(file_name))
                images.append(img_bytes)
    st.write(f"{len(images)}개의 이미지가 ZIP에서 로드됨")

    # PDF 변환 버튼
    if st.button("최대 화질 PDF 변환"):
        with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
            pdf_bytes = enhance_and_create_pdf(images)
        st.success("PDF 변환 완료 ✅")
        st.download_button(
            "PDF 다운로드",
            data=pdf_bytes,
            file_name="converted_highres.pdf"
        )
