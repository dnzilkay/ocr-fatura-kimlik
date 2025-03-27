import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_from_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Görsel yüklenemedi!")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')
    return text
