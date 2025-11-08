from PIL import Image, ImageEnhance, ImageFilter
import io
import img2pdf

def enhance_highres(img):
    """
    이미지 업스케일 + 선명도 + 대비 강화
    """
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=1))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    return img

def enhance_and_create_pdf(uploaded_files):
    """
    다중 이미지 → 최대 화질 PDF 변환
    """
    images_for_pdf = []

    for file in uploaded_files:
        file.seek(0)
        img = Image.open(file).convert("RGB")
        img = enhance_highres(img)

        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=100)  # JPEG 품질 최대
        buf.seek(0)
        images_for_pdf.append(buf)

    # PDF 레이아웃 설정 (300 DPI)
    layout_fun = img2pdf.get_layout_fun(dpi=300)

    pdf_bytes = io.BytesIO(img2pdf.convert([buf for buf in images_for_pdf], layout_fun=layout_fun))
    return pdf_bytes
