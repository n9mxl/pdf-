from pdf2image import convert_from_bytes
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
    pages = convert_from_bytes(pdf_file.read(), dpi=300)
    images_bufs = []

    for page in pages:
        img = page.convert("RGB")
        img = enhance_image(img)

        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=100)
        buf.seek(0)
        images_bufs.append(buf)

    layout_fun = img2pdf.get_layout_fun(dpi=300)
    highres_pdf = io.BytesIO(img2pdf.convert([buf for buf in images_bufs], layout_fun=layout_fun))
    return highres_pdf
