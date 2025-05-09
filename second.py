# extract_no_and_tanggal.py

import os
import re
import fitz  # PyMuPDF
import pandas as pd

# ─── Configuration ─────────────────────────────────────────────────────────────
# Replace this with the path to the folder containing your “_first_page.pdf” files
FOLDER_PATH = os.path.join(os.path.dirname(__file__), "pdf_output")
# ────────────────────────────────────────────────────────────────────────────────

# Regex to capture the number after "No: "
regex_no = re.compile(r"No:\s*(\d+)")
# Regex to capture the date DD Month YYYY before " (\"Tanggal Efektif\")"
regex_date = re.compile(
    r"(\d{1,2}\s+"
    r"(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)"
    r"\s+\d{4})"
    r"(?=\s*\(\"Tanggal Efektif\"\))"
)

def extract_fields_from_first_page(pdf_path):
    """Extracts 'No' and 'Tanggal Efektif' from the first page of a PDF."""
    doc = fitz.open(pdf_path)
    text = doc.load_page(0).get_text("text")
    no_match = regex_no.search(text)
    date_match = regex_date.search(text)
    return (
        no_match.group(1) if no_match else "",
        date_match.group(1) if date_match else ""
    )

if __name__ == "__main__":
    records = []
    for fname in os.listdir(FOLDER_PATH):
        if not fname.endswith("_first_page.pdf"):
            continue
        path = os.path.join(FOLDER_PATH, fname)
        no_val, tanggal_val = extract_fields_from_first_page(path)
        records.append({
            "Filename": fname,
            "No": no_val,
            "Tanggal Efektif": tanggal_val
        })

    # Save to CSV
    df = pd.DataFrame(records)
    output_csv = os.path.join(FOLDER_PATH, "extracted_data.csv")
    df.to_csv(output_csv, index=False)

    print(f"Saved extracted fields to {output_csv}")
