from PIL import Image, ImageEnhance, ImageFilter
import io
import img2pdf

# GPU 환경이면 Real-ESRGAN 적용 가능
# from realesrgan import RealESRGAN
# import torch

def enhance_highres(img):
    # Pillow 업스케일 + 선명도 + 대비 강화
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)

    # GPU 환경 Real-ESRGAN 적용 (선택)
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # model = RealESRGAN(device, scale=2)
    # model.load_weights('weights/RealESRGAN_x2.pth')
    # img = model.predict(img)

    return img

def enhance_and_create_pdf(uploaded_files):
    images_for_pdf = []

    for file in uploaded_files:
        img = Image.open(file).convert("RGB")
        img = enhance_highres(img)

        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        buf.seek(0)
        images_for_pdf.append(buf)

    pdf_bytes = img2pdf.convert([buf for buf in images_for_pdf])
    return pdf_bytes
