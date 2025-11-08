from PIL import Image, ImageEnhance
import io
import img2pdf

def enhance_and_create_pdf(uploaded_files):
    images_bytes = []

    for file in uploaded_files:
        img = Image.open(file)

        # 안전한 화질 개선
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)  # 글자/그림 내용 유지
        img = img.resize((img.width*2, img.height*2), Image.LANCZOS)

        # BytesIO로 저장
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        images_bytes.append(buf)

    # PDF 변환
    pdf_bytes = img2pdf.convert([img.getbuffer() for img in images_bytes])
    return pdf_bytes
