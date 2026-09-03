"""
text_extractor.py
------------------
Job: take a resume FILE (pdf / docx / txt) and return plain raw text.

This is step 1 of the Resume Agent. It doesn't try to understand the
resume yet — it just gets the words out of whatever file format the
user uploaded, so every later step can work with plain text.
"""

import os
import pdfplumber
import docx  # this comes from the "python-docx" package


def extract_text(file_path: str) -> str:
    """
    Detect the file type from its extension and pull out the raw text.

    Args:
        file_path: path to a .pdf, .docx, or .txt resume file

    Returns:
        A single string containing all the text found in the file.
    """
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return _extract_from_pdf(file_path)
    elif extension == ".docx":
        return _extract_from_docx(file_path)
    elif extension == ".txt":
        return _extract_from_txt(file_path)
    else:
        raise ValueError(
            f"Unsupported file type: {extension}. Use .pdf, .docx, or .txt"
        )


def _extract_from_pdf(file_path: str) -> str:
    """Read every page of a PDF and join the text together."""
    full_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # some pages might be blank/images
                full_text.append(page_text)
    return "\n".join(full_text)


def _extract_from_docx(file_path: str) -> str:
    """Read every paragraph of a Word document and join the text together."""
    document = docx.Document(file_path)
    paragraphs = [para.text for para in document.paragraphs]
    return "\n".join(paragraphs)


def _extract_from_txt(file_path: str) -> str:
    """Just read a plain text file directly."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# Quick manual test — only runs if you execute this file directly
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python text_extractor.py <path_to_resume>")
    else:
        text = extract_text(sys.argv[1])
        print(text[:500])  # print first 500 characters as a sanity check
