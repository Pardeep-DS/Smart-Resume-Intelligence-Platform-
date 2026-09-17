# Smart Resume Intelligence Platform

An intelligent resume parsing and analysis pipeline that extracts, structures, and analyzes information from resumes (PDF/DOCX) using Python. The platform breaks a resume down into text, logical sections, and key skills — laying the groundwork for automated candidate screening, resume scoring, and job-fit matching.

## 🚀 Project Overview

Manually reviewing resumes is slow and inconsistent. This project aims to automate the early stages of resume intelligence by:

- Extracting raw text from resume files
- Splitting resumes into meaningful sections (e.g., Education, Experience, Skills, Projects)
- Identifying and extracting relevant technical and soft skills

This is an evolving project — more modules (parsing, scoring, matching, and a UI/API layer) will be added over time.

## 📂 Current Modules

| File | Description |
|------|-------------|
| `text_extractor.py` | Extracts raw text content from resume files (PDF/DOCX) for downstream processing. |
| `section_splitter.py` | Parses the extracted text and splits it into standard resume sections (e.g., Education, Experience, Skills, Certifications). |
| `skills_extractor.py` | Identifies and extracts technical and soft skills from the resume text using keyword/NLP-based matching. |

> Note: This table will be updated as new modules are added to the pipeline.

## 🛠️ Tech Stack

- **Language:** Python
- **Core areas:** Text extraction, NLP, information extraction
- *(Update this section with specific libraries — e.g., PyPDF2, docx2txt, spaCy, regex, scikit-learn — as they're finalized.)*

## 📁 Project Structure

```
Smart-Resume-Intelligence-Platform/
│
├── text_extractor.py       # Extracts raw text from resume files
├── section_splitter.py     # Splits resume text into sections
├── skills_extractor.py     # Extracts skills from resume text
└── README.md                # Project documentation
```

## ⚙️ Installation

```bash
git clone https://github.com/Pardeep-DS/Smart-Resume-Intelligence-Platform-.git
cd Smart-Resume-Intelligence-Platform-
pip install -r requirements.txt
```

## ▶️ Usage

```python
from text_extractor import extract_text
from section_splitter import split_sections
from skills_extractor import extract_skills

# Step 1: Extract raw text from a resume
raw_text = extract_text("sample_resume.pdf")

# Step 2: Split the resume into sections
sections = split_sections(raw_text)

# Step 3: Extract skills
skills = extract_skills(sections)

print(skills)
```

> Update the usage example above once function signatures are finalized.

## 🗺️ Roadmap

- [x] Text extraction from resumes
- [x] Section-wise resume splitting
- [x] Skills extraction
- [ ] Resume scoring / ranking module
- [ ] Job description matching
- [ ] API layer for integration
- [ ] Simple web UI for demo purposes

## 🤝 Contributing

This is currently a solo learning/portfolio project, but suggestions and feedback are welcome via issues or pull requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

