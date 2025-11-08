import streamlit as st
from pdf_generator import enhance_and_create_pdf
import zipfile
import io

st.set_page_config(page_title="이미지 → ZIP → PDF 변환기", layout="wide")
st.title("📚 이미지 → ZIP → PDF 변환기 (CPU 전용)")

tabs = st.tabs(["1단계: 이미지 → ZIP", "2단계: ZIP → PDF"])

# ===============================
# 1단계: 이미지 → ZIP
# ===============================
with tabs[0]:
    st.header("1단계: 이미지 → ZIP 생성")
    uploaded_files = st.file_uploader(
        "이미지 업로드 (여러 장 선택 가능, 최대 40장 이상 가능)", 
        type=["png","jpg","jpeg"], 
        accept_multiple_files=True,
        key="step1"
    )

    if uploaded_files:
        if st.button("ZIP 파일 생성", key="zip_button"):
            zip_buf = io.BytesIO()
            with zipfile.ZipFile(zip_buf, "w") as zf:
                for file in uploaded_files:
                    file.seek(0)
                    zf.writestr(file.name, file.read())
            zip_buf.seek(0)
            st.success("ZIP 생성 완료 ✅")
            st.download_button(
                "ZIP 다운로드",
                data=zip_buf,
                file_name="images.zip"
            )

# ===============================
# 2단계: ZIP → PDF
# ===============================
with tabs[1]:
    st.header("2단계: ZIP → PDF 변환")
    uploaded_zip = st.file_uploader("ZIP 파일 업로드", type=["zip"], key="step2")
    images = []

    if uploaded_zip:
        with zipfile.ZipFile(uploaded_zip) as z:
            for file_name in z.namelist():
                if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                    img_bytes = io.BytesIO(z.read(file_name))
                    images.append(img_bytes)
        st.write(f"{len(images)}개의 이미지가 ZIP에서 로드됨")

        if st.button("PDF 변환", key="pdf_button"):
            with st.spinner("PDF 변환 중... 잠시만 기다려주세요"):
                pdf_bytes = enhance_and_create_pdf(images)
            st.success("PDF 변환 완료 ✅")
            st.download_button(
                "PDF 다운로드",
                data=pdf_bytes,
                file_name="교과서_highres.pdf"
            )
