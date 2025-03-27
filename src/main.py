import os
from ocr_reader import ocr_from_image
from info_extractor import extract_info
from output_writer import save_as_json, save_as_csv

base_dir = os.path.dirname(os.getcwd())
image_path = os.path.join(base_dir, "data", "ocr-receipts-text-detection", "images", "1.jpg")

print(f"📸 OCR yapılacak dosya: {image_path}")

# OCR işlemi
ocr_text = ocr_from_image(image_path)

# Bilgi çıkarma
info = extract_info(ocr_text)

# Çıktıyı yaz
print("\n📄 OCR'dan Çıkan Bilgiler:")
for key, value in info.items():
    print(f"{key}: {value}")

# kaydet
save_as_json(info)
save_as_csv(info)
