"""
Ana Program Dosyası
OCR işlemlerini yönetir ve örnek kullanım sağlar.
"""

import os
import sys
from ocr_reader import ocr_from_image
from info_extractor import extract_info
from output_writer import save_as_json, save_as_csv
from config import IMAGES_DIR


def process_single_image(image_path: str, save_output: bool = True):
    """
    Tek bir görseli işler.
    
    Args:
        image_path (str): Görsel dosyasının yolu
        save_output (bool): Sonuçları kaydet
        
    Returns:
        dict: Çıkarılan bilgiler
    """
    print(f"\nOCR yapılacak dosya: {image_path}")
    
    try:
        # OCR işlemi
        ocr_text = ocr_from_image(image_path)
        print(f"\nOCR Ham Metni:\n{'-'*50}\n{ocr_text}\n{'-'*50}")
        
        # Bilgi çıkarma
        info = extract_info(ocr_text)
        
        # Çıktıyı göster
        print("\nOCR'dan Çıkan Bilgiler:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        
        # Kaydet
        if save_output:
            save_as_json(info)
            save_as_csv(info)
        
        return info
        
    except Exception as e:
        print(f"HATA: {str(e)}")
        return None


def process_batch_images(image_dir: str, save_output: bool = True):
    """
    Bir dizindeki tüm görselleri işler.
    
    Args:
        image_dir (str): Görsel dizini
        save_output (bool): Sonuçları kaydet
        
    Returns:
        list: Tüm sonuçların listesi
    """
    from config import IMAGE_EXTENSIONS
    
    results = []
    image_files = [f for f in os.listdir(image_dir) 
                   if os.path.splitext(f.lower())[1] in IMAGE_EXTENSIONS]
    
    print(f"\n{len(image_files)} adet görsel bulundu.")
    
    for idx, image_file in enumerate(image_files, 1):
        image_path = os.path.join(image_dir, image_file)
        print(f"\n[{idx}/{len(image_files)}] İşleniyor: {image_file}")
        
        result = process_single_image(image_path, save_output=False)
        if result:
            result['dosya_adi'] = image_file
            results.append(result)
    
    if save_output and results:
        from output_writer import save_batch_as_json
        save_batch_as_json(results, "ocr_batch_output.json")
        
        import pandas as pd
        df = pd.DataFrame(results)
        df.to_csv(os.path.join(os.path.dirname(__file__), "..", "outputs", "ocr_batch_output.csv"), 
                  index=False, encoding="utf-8-sig")
        print("\nToplu sonuçlar kaydedildi.")
    
    return results


def main():
    """Ana fonksiyon"""
    
    # Örnek: Tek görsel işleme
    default_image = os.path.join(IMAGES_DIR, "1.jpg")
    
    if os.path.exists(default_image):
        process_single_image(default_image)
    else:
        print(f"UYARI: Örnek görsel bulunamadı: {default_image}")
        print("Lütfen data/ocr-receipts-text-detection/images/ dizininde görseller bulunduğundan emin olun.")


if __name__ == "__main__":
    main()
