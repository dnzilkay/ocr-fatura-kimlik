"""
Info Extractor Module
OCR metninden anlamlı bilgileri çıkarır.
"""

import re
from typing import Dict, Optional


def safe_regex_search(pattern: str, text: str, group: int = 0) -> Optional[str]:
    """
    Regex araması yapar, bulunamazsa None döner.
    
    Args:
        pattern (str): Regex deseni
        text (str): Aranacak metin
        group (int): Döndürülecek grup numarası
        
    Returns:
        Optional[str]: Bulunan eşleşme veya None
    """
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(group) if match else None


def extract_info(ocr_text: str) -> Dict[str, Optional[str]]:
    """
    OCR metninden fatura/fiş bilgilerini çıkarır.
    
    Args:
        ocr_text (str): OCR ile okunmuş ham metin
        
    Returns:
        Dict[str, Optional[str]]: Çıkarılan bilgiler sözlüğü
    """
    return {
        "Tarih": extract_date(ocr_text),
        "Saat": extract_time(ocr_text),
        "Toplam": extract_total(ocr_text),
        "Nakit": extract_cash(ocr_text),
        "Para Üstü": extract_change(ocr_text),
        "Fiş No": extract_receipt_number(ocr_text)
    }


def extract_date(text: str) -> Optional[str]:
    """Tarih bilgisini çıkarır (DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY formatları)"""
    patterns = [
        r"\d{2}[-/\.]\d{2}[-/\.]\d{4}",  # DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY
        r"\d{4}[-/\.]\d{2}[-/\.]\d{2}",  # YYYY-MM-DD
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text)
        if result:
            return result
    return None


def extract_time(text: str) -> Optional[str]:
    """Saat bilgisini çıkarır"""
    patterns = [
        r"\d{1,2}:\d{2}(?::\d{2})?\s*[AP]M",  # 12:30 PM, 12:30:45 PM
        r"\d{1,2}:\d{2}(?::\d{2})?",  # 14:30, 14:30:45
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text)
        if result:
            return result
    return None


def extract_total(text: str) -> Optional[str]:
    """Toplam tutarı çıkarır"""
    patterns = [
        r"(?:TOTAL|TOPLAM|SUM|TUTAR)\s*:?\s*\$?\s*([\d.,]+)",
        r"(?:TOTAL|TOPLAM)\s*\$?\s*([\d.,]+)",
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=1)
        if result:
            return result
    return None


def extract_cash(text: str) -> Optional[str]:
    """Nakit tutarını çıkarır"""
    patterns = [
        r"(?:CASH|NAKİT|NAKIT)\s*:?\s*\$?\s*([\d.,]+)",
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=1)
        if result:
            return result
    return None


def extract_change(text: str) -> Optional[str]:
    """Para üstü tutarını çıkarır"""
    patterns = [
        r"(?:CHANGE|PARA\s*ÜSTÜ|PARA\s*USTU)\s*:?\s*\$?\s*([\d.,]+)",
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=1)
        if result:
            return result
    return None


def extract_receipt_number(text: str) -> Optional[str]:
    """Fiş numarasını çıkarır"""
    patterns = [
        r"\d{4}\s\d{2}\s\d{4}\s\d{4}",  # 1234 56 7890 1234
        r"(?:NO|NUM|#)\s*:?\s*(\d+)",  # NO: 12345, #12345
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=0)
        if result:
            return result
    return None


def extract_tc_number(text: str) -> Optional[str]:
    """TC Kimlik numarasını çıkarır (11 haneli)"""
    pattern = r"\b[1-9]\d{10}\b"  # 11 haneli, ilk hane 0 olamaz
    return safe_regex_search(pattern, text)


def extract_name(text: str) -> Optional[str]:
    """İsim bilgisini çıkarır"""
    patterns = [
        r"(?:ADI|AD|NAME)\s*:?\s*([A-ZÇĞİÖŞÜ\s]+)",
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=1)
        if result:
            return result.strip()
    return None


def extract_surname(text: str) -> Optional[str]:
    """Soyisim bilgisini çıkarır"""
    patterns = [
        r"(?:SOYADI|SOYAD|SURNAME)\s*:?\s*([A-ZÇĞİÖŞÜ\s]+)",
    ]
    for pattern in patterns:
        result = safe_regex_search(pattern, text, group=1)
        if result:
            return result.strip()
    return None
