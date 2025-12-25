"""
Output Writer Module
İşlenmiş verileri farklı formatlarda kaydeder.
"""

import json
import os
import pandas as pd
from typing import Dict, Any
from config import OUTPUT_DIR


def ensure_output_dir():
    """Çıktı dizininin varlığını kontrol eder, yoksa oluşturur."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_as_json(data: Dict[str, Any], filename: str = "ocr_output.json") -> str:
    """
    Veriyi JSON formatında kaydeder.
    
    Args:
        data (Dict): Kaydedilecek veri
        filename (str): Dosya adı
        
    Returns:
        str: Kaydedilen dosyanın tam yolu
    """
    ensure_output_dir()
    
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"JSON dosyası kaydedildi: {file_path}")
    return file_path


def save_as_csv(data: Dict[str, Any], filename: str = "ocr_output.csv") -> str:
    """
    Veriyi CSV formatında kaydeder.
    
    Args:
        data (Dict): Kaydedilecek veri
        filename (str): Dosya adı
        
    Returns:
        str: Kaydedilen dosyanın tam yolu
    """
    ensure_output_dir()
    
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    df = pd.DataFrame([data])  # Dict'ten tek satırlık DataFrame
    df.to_csv(file_path, index=False, encoding="utf-8-sig")
    
    print(f" CSV dosyası kaydedildi: {file_path}")
    return file_path


def append_to_csv(data: Dict[str, Any], filename: str = "ocr_output.csv") -> str:
    """
    Veriyi mevcut CSV dosyasına ekler (varsa).
    
    Args:
        data (Dict): Eklenecek veri
        filename (str): Dosya adı
        
    Returns:
        str: Kaydedilen dosyanın tam yolu
    """
    ensure_output_dir()
    
    file_path = os.path.join(OUTPUT_DIR, filename)
    df = pd.DataFrame([data])
    
    # Dosya varsa ekle, yoksa yeni oluştur
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False, encoding="utf-8-sig")
        print(f" CSV dosyasına eklendi: {file_path}")
    else:
        df.to_csv(file_path, index=False, encoding="utf-8-sig")
        print(f" Yeni CSV dosyası oluşturuldu: {file_path}")
    
    return file_path


def save_batch_as_json(data_list: list, filename: str = "ocr_batch_output.json") -> str:
    """
    Birden fazla veriyi JSON array olarak kaydeder.
    
    Args:
        data_list (list): Kaydedilecek veri listesi
        filename (str): Dosya adı
        
    Returns:
        str: Kaydedilen dosyanın tam yolu
    """
    ensure_output_dir()
    
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)
    
    print(f" Toplu JSON dosyası kaydedildi: {file_path}")
    return file_path