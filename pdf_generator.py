from PIL import Image, ImageEnhance
import io
import img2pdf

def enhance_and_create_pdf(uploaded_files):
    images_for_pdf = []

    for file in uploaded_files:
        img = Image.open(file)

        # 화질 개선
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)
        img = img.resize((img.width*2, img.height*2), Image.LANCZOS)

        # PDF 변환용 BytesIO (RGB JPEG)
        buf = io.BytesIO()
        img.convert("RGB").save(buf, format="JPEG")
        buf.seek(0)
        images_for_pdf.append(buf)

    # PDF 변환
    pdf_bytes = img2pdf.convert([buf for buf in images_for_pdf])
    return pdf_bytes
