"""
section_splitter.py
--------------------
Job: split the raw resume text into labeled chunks — Education,
Experience, Projects, Skills, Certifications — using common section
header patterns.

Resumes don't follow one fixed format, so this uses a list of likely
header spellings per section. It's a heuristic, not perfect — that's
normal for v1. You can improve this later with real NLP.
"""

import re

# Each section can be titled a few different ways in real resumes.
SECTION_HEADERS = {
    "education": ["education", "academic background", "qualifications"],
    "experience": ["experience", "work experience", "employment history", "professional experience"],
    "projects": ["projects", "academic projects", "personal projects"],
    "skills": ["skills", "technical skills", "core competencies"],
    "certifications": ["certifications", "certificates", "licenses"],
}


def split_into_sections(text: str) -> dict:
    """
    Split resume text into a dictionary of {section_name: section_text}.

    Approach:
      1. Go line by line.
      2. If a line looks like a section header (short line, matches one
         of our known header words), start a new section.
      3. Otherwise, keep appending the line to whichever section is
         currently active.

    Returns:
        dict like {"education": "...", "experience": "...", ...}
        Any text before the first recognized header goes into "header"
        (usually name, contact info, summary).
    """
    lines = text.split("\n")
    sections = {"header": []}
    current_section = "header"

    for line in lines:
        stripped = line.strip()
        matched_section = _match_section_header(stripped)

        if matched_section:
            current_section = matched_section
            sections.setdefault(current_section, [])
            continue  # don't include the header line itself in the content

        if stripped:  # skip empty lines
            sections.setdefault(current_section, []).append(stripped)

    # Join each section's lines back into one text block
    return {name: "\n".join(content) for name, content in sections.items()}


def _match_section_header(line: str) -> str:
    """
    Check if a line looks like a section header.
    Heuristic: short line (under 40 chars) whose lowercase text matches
    one of our known header phrases.
    """
    if not line or len(line) > 40:
        return None

    lowered = line.lower().strip(":").strip()

    for section_name, possible_headers in SECTION_HEADERS.items():
        if lowered in possible_headers:
            return section_name

    return None


# Quick manual test
if __name__ == "__main__":
    sample = """John Doe
    john@email.com

    Education
    BCA, SSM College, 2026

    Skills
    Python, SQL, Power BI

    Experience
    Intern at XYZ Corp - built dashboards
    """
    result = split_into_sections(sample)
    for section, content in result.items():
        print(f"--- {section} ---")
        print(content)
        print()
