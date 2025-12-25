# OCR Fatura ve Kimlik Okuma Projesi

Bu proje, görsel formattaki **fatura, fiş ve kimlik belgelerinden** otomatik olarak bilgi çıkarmak için geliştirilmiş bir Python uygulamasıdır. Tesseract OCR ve OpenCV kullanarak metinleri okur, işler ve yapılandırılmış veri olarak sunar.

## Özellikler

- **Faturalardan bilgi çıkarma**: Tarih, tutar, fatura no
- **Kimliklerden bilgi çıkarma**: Ad, soyad, TC kimlik no
- **Görüntü ön işleme**: Kontrast artırma, gürültü azaltma
- **Çoklu format desteği**: JSON ve CSV çıktı
- **Cross-platform**: Windows, macOS, Linux desteği

## Gereksinimler

- Python 3.8+
- Tesseract OCR

## Kurulum

### 1. Tesseract Kurulumu

**Windows:**
```bash
choco install tesseract
```

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt install tesseract-ocr
```

### 2. Python Bağımlılıkları

```bash
pip install -r requirements.txt
```

## Kullanım

```python
from src.main import process_single_image

# Tek bir görseli işle
result = process_single_image("data/ornek.jpg")
```

## Proje Yapısı

```
ocr-fatura-kimlik/
├── src/                    # Kaynak kodlar
│   ├── config.py          # Konfigürasyon
│   ├── main.py            # Ana program
│   ├── ocr_reader.py      # OCR okuma
│   ├── info_extractor.py  # Bilgi çıkarma
│   └── output_writer.py   # Çıktı yazma
├── data/                  # Veri klasörü
├── outputs/               # OCR çıktıları
└── requirements.txt       # Bağımlılıklar
```

## Lisans

MIT License - Detaylar için [LICENSE](LICENSE) dosyasına bakın.
