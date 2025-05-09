# extract_first_pages.py

import os
import sys
import subprocess

# Install required modules from requirements_notes.txt if not already installed
def install_requirements():
    req_file = os.path.join(os.path.dirname(__file__), "requirements_notes.txt")
    if not os.path.exists(req_file):
        return
    with open(req_file) as f:
        pkgs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    for pkg in pkgs:
        try:
            __import__(pkg.split()[0])
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

install_requirements()

from PyPDF2 import PdfReader, PdfWriter

# ─── Configuration ─────────────────────────────────────────────────────────────
# Input and output folders within the repo
FOLDER_PATH = os.path.join(os.path.dirname(__file__), "pdf_input")
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "pdf_output")

# List the two PDF filenames (ensure they match exactly)
pdf_files = [
    "20250430T133332_Akad__7005384.pdf",
    "20240730T071712_Akad_Kapas_5267318.pdf"
]
# ────────────────────────────────────────────────────────────────────────────────

def extract_first_page(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    # grab the very first page
    writer.add_page(reader.pages[0])
    # write it out
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

if __name__ == "__main__":
    # Ensure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for fname in pdf_files:
        in_pdf = os.path.join(FOLDER_PATH, fname)
        base, _ = os.path.splitext(fname)
        out_pdf = os.path.join(OUTPUT_FOLDER, f"{base}_first_page.pdf")
        extract_first_page(in_pdf, out_pdf)
        print(f"Extracted first page of {fname} → {os.path.basename(out_pdf)}")
