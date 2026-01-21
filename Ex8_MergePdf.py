"""
================================================================================
Project      : PDF Manipulation with PyPDF
File         : Ex8_MergePdf.py
Author       : Shahroze
Date         : 22-Jan-2026
Python       : 3.14
Libraries    : pypdf, os
Description :
    This script demonstrates how to:
        - Read and extract text from PDFs using PyPDF
        - Split a PDF into chapters based on page ranges
        - Merge multiple PDFs back into a single PDF
        - Add metadata (author, title) to PDFs
    The example uses 'The Adventures of Sherlock Holmes' for splitting and merging.
Usage :
    - Adjust 'pdf_path' to your PDF file path
    - Define chapter page ranges in 'chapters' dictionary
    - Run script to create chapter PDFs and merge them back
Output :
    - Individual chapter PDFs in the specified 'out_dir'
    - Merged PDF in 'final_pdf' with metadata
================================================================================
"""

"""
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files
into a single pdf. You're welcome to add more functionalities.
pyPDF is a free and open_source pure_Python PDF library capable of splitting, merging, rotate pages, cropping and transforming 
the pages of pdf files. It can also add custom data, viewing options and passwords to pdf files. pyPDF can retrieve
text and metadata from PDFs as well.
Think of PyPDF as a PDF manipulator, not a PDF creator. It does not design layouts like ReportLab. It works with existing PDFs.

Key things you can do with PyPDF :
- Read PDF files
  - PdfReader
  - reader.pages
  - reader.metadata
- Extract text from pages
  - page.extract_text()
- Writing and modifying pdf
  - PdfWriter
  - writer.add_page(page)
  - writer.write(file)
- Merge multiple PDFs into one
  - PdfMerger
- Split PDFs into separate files
- Rotate pages
  - page.rotate(90)
- Encrypt and decrypt PDFs
  - Encrypt PDFs with passwords
  - Decrypt protected PDFs (if you know the password)
- Access metadata like author or title
  - Read metadata (author, title)
  - Modify metadata
  writer.add_metadata({
    "/Author": "Shahroze",
    "/Title": "Merged Report"
})

"""
import os
os.system('cls')

# # load the PDF
# reader = PdfReader(r"C:\Users\dell\Documents\E-Commerce Management\Rich-dad-poor-dad.pdf")

# # total number of pages
# print("Total pages:", len(reader.pages))

# # read first page
# first_page = reader.pages[0]
# text = first_page.extract_text()

# print("\n--- First Page Text ---")
import pypdf
from pypdf import PdfReader, PdfWriter
pdf_path = r"C:\Users\dell\Documents\pypdf module\Sherlock_Holmes.pdf"
reader = PdfReader(pdf_path)
print("Total pages:", len(reader.pages))
for i in range(10):  # first 10 pages only
    text = reader.pages[i].extract_text()
    print(f"\n--- Page {i} ---")
    print(text[:300] if text else "No text found")

# Chapter 1 starts at page 5
# Chapter 2 starts at page 9
# Chapter 3 starts at page 14

# Splitting the book into chapters
out_dir = r"C:\Users\dell\Documents\Sherlock_Holmes_Chapters"
os.makedirs(out_dir, exist_ok=True)
reader = PdfReader(pdf_path)
# Replace with real page numbers
chapters = {
    "Chapter_01": (8, 12),
    "Chapter_02": (12, 17),
    "Chapter_03": (17, 18),
}
for name, (start, end) in chapters.items():
    writer = PdfWriter()
    for page_num in range(start, end + 1):
        writer.add_page(reader.pages[page_num])

    output_path = os.path.join(out_dir, f"{name}.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"{name} created successfully")


# Merge all chapters back into one book
chapters_dir = r"C:\Users\dell\Documents\pypdf module\Sherlock_Holmes_Chapters"
final_pdf = r"C:\Users\dell\Documents\Sherlock_Holmes_Merged.pdf"

writer = PdfWriter()

for file in sorted(os.listdir(chapters_dir)):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(chapters_dir, file))
        for page in reader.pages:
            writer.add_page(page)

writer.add_metadata({
    "/Author": "Conan Doyle",
    "/Title": "The Adventures of Sherlock Holmes (Merged)"
})

with open(final_pdf, "wb") as f:
    writer.write(f)

print("Final book merged successfully")








