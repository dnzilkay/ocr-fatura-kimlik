"""
OCR Reader Module
Görsellerden metin okuma işlemlerini gerçekleştirir.
"""

import pytesseract
import cv2
from config import TESSERACT_PATH, DEFAULT_LANG

# Tesseract yolunu ayarla (sadece gerekirse)
if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def ocr_from_image(image_path, lang=DEFAULT_LANG, preprocess=True):
    """
    Görsel dosyasından OCR ile metin okur.
    
    Args:
        image_path (str): Okunacak görsel dosyasının yolu
        lang (str): OCR dili (varsayılan: 'eng')
        preprocess (bool): Görüntü ön işleme yapılsın mı?
        
    Returns:
        str: OCR ile okunan metin
        
    Raises:
        FileNotFoundError: Görsel dosyası bulunamazsa
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Görsel yüklenemedi: {image_path}")

    if preprocess:
        # Görüntü ön işleme
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Kontrast artırma
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    text = pytesseract.image_to_string(gray, lang=lang)
    return text


def ocr_from_image_with_boxes(image_path, lang=DEFAULT_LANG):
    """
    Görsel dosyasından OCR ile metin ve konum bilgilerini okur.
    
    Args:
        image_path (str): Okunacak görsel dosyasının yolu
        lang (str): OCR dili
        
    Returns:
        dict: Her kelime için metin ve konum bilgileri
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Görsel yüklenemedi: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detaylı OCR çıktısı al
    data = pytesseract.image_to_data(gray, lang=lang, output_type=pytesseract.Output.DICT)
    
    return data
