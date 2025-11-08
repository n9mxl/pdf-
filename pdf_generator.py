import fitz  # PyMuPDF
from PIL import Image, ImageEnhance, ImageFilter
import io
import img2pdf

def enhance_image(img):
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=1))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    return img

def enhance_pdf(pdf_file):
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    images_bufs = []

    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = enhance_image(img)

        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=100)
        buf.seek(0)
        images_bufs.append(buf)

    highres_pdf = io.BytesIO(img2pdf.convert([buf for buf in images_bufs], dpi=300))
    return highres_pdf
