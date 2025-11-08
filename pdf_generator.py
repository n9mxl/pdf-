from PIL import Image, ImageEnhance
import io
import img2pdf

# Real-ESRGAN 사용 예시
# from realesrgan import RealESRGAN
# import torch

def enhance_and_create_pdf(uploaded_files):
    images_bytes = []

    # # Real-ESRGAN 초기화 (GPU 사용 가능 시)
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # model = RealESRGAN(device, scale=2)
    # model.load_weights('models/RealESRGAN_x2.pth')

    for file in uploaded_files:
        img = Image.open(file)

        # Pillow 기본 화질 개선 (선명도 + 확대)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)  # 글자 유지, 선명도 향상
        img = img.resize((img.width*2, img.height*2), Image.LANCZOS)

        # Real-ESRGAN 사용 시
        # img = model.predict(img)

        # 메모리용 BytesIO
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        images_bytes.append(buf)

    # PDF 변환
    pdf_bytes = img2pdf.convert([img.getbuffer() for img in images_bytes])
    return pdf_bytes
