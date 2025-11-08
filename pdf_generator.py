from PIL import Image, ImageEnhance, ImageFilter
import io
import img2pdf

def enhance_highres(img):
    # Pillow 업스케일 + 선명도 + 대비 강화
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)
    return img

def enhance_and_create_pdf(uploaded_files):
    images_for_pdf = []

    for file in uploaded_files:
        file.seek(0)  # Streamlit 업로드 파일 위치 초기화
        img = Image.open(file).convert("RGB")
        img = enhance_highres(img)

        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        buf.seek(0)
        images_for_pdf.append(buf)

    pdf_bytes = io.BytesIO(img2pdf.convert([buf for buf in images_for_pdf]))
    return pdf_bytes
