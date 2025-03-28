# 🧾 OCR ile Fatura ve Kimlik Bilgisi Okuma Deneme Uygulaması👑

Bu proje, görsel formatta gelen **fatura ve kimlik belgelerinden** otomatik olarak bilgi çekmek için geliştirilmiştir.  
`Python`, `Tesseract OCR` ve `OpenCV` gibi teknolojiler kullanılarak, metinler okunur, işlenir ve çıktı olarak kaydedilir.
Bu proje görüntü işleme ile ilgili fikir sahibi olabilmek için yapıldı.

## 🚀 Özellikler
- Faturalardan: Tarih, tutar, fatura no çıkarma
- Kimliklerden: Ad, soyad, TC kimlik no ayıklama
- Görsel ön işleme ve metin temizleme
- JSON / CSV formatında çıktı üretme

## 🛠️ Kullanılan Teknolojiler
- Python 🐍
- pytesseract
- OpenCV
- Pillow
- Pandas

## 📂 Dosya Yapısı
- data/ -> Örnek görseller
- src/ -> Tüm kod dosyaları
- outputs/ -> OCR çıktıları
