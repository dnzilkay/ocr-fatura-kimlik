import re

def extract_info(ocr_text):
    return {
        "Tarih": re.search(r"\d{2}-\d{2}-\d{4}", ocr_text).group() if re.search(r"\d{2}-\d{2}-\d{4}", ocr_text) else None,
        "Saat": re.search(r"\d{1,2}:\d{2}[AP]M", ocr_text).group() if re.search(r"\d{1,2}:\d{2}[AP]M", ocr_text) else None,
        "Toplam": re.search(r"TOTAL\s*\$?\s*([\d.,]+)", ocr_text).group(1) if re.search(r"TOTAL\s*\$?\s*([\d.,]+)", ocr_text) else None,
        "Nakit": re.search(r"CASH\s*\$?\s*([\d.,]+)", ocr_text).group(1) if re.search(r"CASH\s*\$?\s*([\d.,]+)", ocr_text) else None,
        "Para Üstü": re.search(r"CHANGE\s*\$?\s*([\d.,]+)", ocr_text).group(1) if re.search(r"CHANGE\s*\$?\s*([\d.,]+)", ocr_text) else None,
        "Fiş No": re.search(r"\d{4}\s\d{2}\s\d{4}\s\d{4}", ocr_text).group() if re.search(r"\d{4}\s\d{2}\s\d{4}\s\d{4}", ocr_text) else None
    }
