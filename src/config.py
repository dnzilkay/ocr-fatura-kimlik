"""
Konfigürasyon Ayarları
Bu dosya projenin genel ayarlarını içerir.
"""

import os
import platform

# Proje kök dizini
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dizin yapısı
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")
IMAGES_DIR = os.path.join(DATA_DIR, "ocr-receipts-text-detection", "images")

# Tesseract ayarları - Platform bazlı otomatik tespit
def get_tesseract_path():
    """
    İşletim sistemine göre Tesseract yolunu otomatik belirler.
    Eğer bulunamazsa None döner ve sistem PATH'inden aranır.
    """
    system = platform.system()
    
    if system == "Windows":
        possible_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
    
    elif system == "Darwin":  # macOS
        possible_paths = [
            "/usr/local/bin/tesseract",
            "/opt/homebrew/bin/tesseract",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
    
    elif system == "Linux":
        possible_paths = [
            "/usr/bin/tesseract",
            "/usr/local/bin/tesseract",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
    
    # Eğer hiçbiri bulunamazsa None döner (sistem PATH kullanılır)
    return None

TESSERACT_PATH = get_tesseract_path()

# OCR ayarları
DEFAULT_LANG = 'eng'  # Varsayılan dil (İngilizce)
SUPPORTED_LANGS = ['eng', 'tur']  # Desteklenen diller

# Görüntü işleme ayarları
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

# Çıktı formatları
OUTPUT_FORMATS = ['json', 'csv']

# Loglama ayarları
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

