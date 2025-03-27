import json
import os
import pandas as pd

def save_as_json(data, filename="ocr_output.json"):
    output_dir = os.path.join(os.path.dirname(os.getcwd()), "outputs")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"💾 JSON dosyası kaydedildi: {file_path}")

def save_as_csv(data, filename="ocr_output.csv"):
    output_dir = os.path.join(os.path.dirname(os.getcwd()), "outputs")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)

    df = pd.DataFrame([data])  # Dict'ten tek satırlık DataFrame
    df.to_csv(file_path, index=False, encoding="utf-8-sig")

    print(f"📊 CSV dosyası kaydedildi: {file_path}")