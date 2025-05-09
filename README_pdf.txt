PDF Extraction Workflow - Instructions
======================================

1. Place Input PDFs
-------------------
- Upload or copy all relevant PDF files you want to process into the `pdf_input` folder in this repository.

2. Extract First Pages
----------------------
- Run the script `first.py`.
- This script will:
  - Automatically install any required Python modules (PyPDF2, PyMuPDF, pandas) if they are not already installed.
  - Extract the first page from each PDF listed in the `pdf_files` variable.
  - Save the resulting single-page PDFs into the `pdf_output` folder, with filenames ending in `_first_page.pdf`.

3. Extract "No" and "Tanggal Efektif" Fields
--------------------------------------------
- Run the script `second.py`.
- This script will:
  - Scan all files in the `pdf_output` folder ending with `_first_page.pdf`.
  - Extract the "No" and "Tanggal Efektif" fields from the first page of each PDF.
  - Save the extracted data into a CSV file named `extracted_data.csv` inside the `pdf_output` folder.

4. Review Results
-----------------
- The extracted first pages are in `pdf_output`.
- The CSV file `extracted_data.csv` in `pdf_output` contains the extracted fields for all processed PDFs.

Notes
-----
- Make sure your input PDF filenames match those listed in the `pdf_files` variable in `first.py`.
- You can edit `pdf_files` in `first.py` to add or remove files as needed.
- All scripts are designed to be run from the root of this repository.
