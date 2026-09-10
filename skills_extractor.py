"""
skills_extractor.py
--------------------
Job: given raw resume text, find which skills (from our taxonomy) appear
in it.

This uses simple, explainable keyword matching rather than a heavy NLP
model — good enough for v1, easy to debug, and easy to explain in an
interview ("I used a curated skills taxonomy with word-boundary regex
matching to avoid false positives like matching 'R' inside 'Robert'").
"""

import json
import re


def load_skills_taxonomy(taxonomy_path: str = "skills_taxonomy.json") -> list:
    """
    Load the skills taxonomy JSON and flatten it into one simple list
    of skill names (we don't need the categories for matching, just
    for later grouping/display).
    """
    with open(taxonomy_path, "r", encoding="utf-8") as f:
        categorized = json.load(f)

    all_skills = []
    for category_skills in categorized.values():
        all_skills.extend(category_skills)
    return all_skills


def extract_skills(text: str, taxonomy_path: str = "skills_taxonomy.json") -> list:
    """
    Scan the resume text and return every skill from the taxonomy that
    appears in it.

    Args:
        text: raw resume text
        taxonomy_path: path to the skills taxonomy JSON file

    Returns:
        A sorted list of matched skill names, e.g. ["Pandas", "Power BI", "Python", "SQL"]
    """
    all_skills = load_skills_taxonomy(taxonomy_path)
    found_skills = set()

    for skill in all_skills:
        # \b = word boundary, so "R" won't match inside "Robert"
        # re.escape handles skills with special characters like "C++"
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text, flags=re.IGNORECASE):
            found_skills.add(skill)

    return sorted(found_skills)


# Quick manual test
if __name__ == "__main__":
    sample_text = """
    Experienced in Python, SQL and Power BI. Built machine learning
    models using Scikit-learn and Pandas. Familiar with Git and Docker.
    """
    print(extract_skills(sample_text))
