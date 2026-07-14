# 📄 Premium AI Resume Analyzer

<p align="center">
  <b>Advanced ATS Resume Analysis & Candidate Dashboard</b><br>
  Analyze PDF and DOCX resumes against job descriptions using spaCy NLP, save evaluation histories to SQLite, and export professional PDF reports.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/spaCy-NLP%20Engine-09A3D5?style=for-the-badge&logo=spacy&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/ReportLab-PDF%20Generator-red?style=for-the-badge">
</p>

---

## 📖 Overview

AI Resume Analyzer is a premium Streamlit web application that evaluates how closely a resume matches a job description. The application parses uploaded PDF and DOCX files, extracts technical skill keywords intelligently via NLP, compares them against required skills, and generates an Applicant Tracking System (ATS) compatibility score.

This version features **user authentication (secure signup/login)**, a **saved reports history dashboard**, **profile skill management**, and **professional PDF report exporting**.

---

## ✨ Features

* 📄 **Multi-Format Uploads**: Support for both **PDF** (via PyMuPDF) and **DOCX** (via python-docx) resume files.
* 🧠 **Intelligent NLP Skill Matcher**: Uses **spaCy's PhraseMatcher** to match skills accurately by respecting token boundaries (preventing false positives like matching "c" in "excel" or "docker").
* 🔒 **Secure User Authentication**: Hashed PBKDF2 password authentication and session management.
* 👤 **Candidate Skill Profile**: Profile page to manage your personal target skills list and professional summary.
* 📋 **Reports History Dashboard**: Logged-in users can browse all past analysis scores, review details, download past reports, and delete records.
* 📥 **Export to PDF**: Generate and download professional PDF analysis reports featuring matching status, scores, and formatted suggestions.
* 🎨 **Premium Glassmorphic UI**: Streamlined interface with visual cards, metrics, and progress bars.

---

## 🛠 Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Programming Language |
| **Streamlit** | Web App Interface & Session State Management |
| **spaCy (en_core_web_sm)** | NLP Tokenizer & PhraseMatcher |
| **SQLite** | Hashed User Accounts & Analysis History Storage |
| **PyMuPDF & python-docx** | Document Parsing |
| **ReportLab** | Dynamic PDF Report Compilation |

---

## 📂 Project Structure

```text
ResumeAnalyzer/
│
├── app.py               # Main Streamlit Application
├── database.py          # SQLite database connection & account operations
├── pdf_generator.py     # ReportLab PDF building rules
├── requirements.txt     # Python package requirements
├── README.md            # Project description & usage guide
├── .env                 # Environment variables
└── resume_analyzer.db   # Local SQLite Database (auto-generated)
```

---

## ⚙️ Installation & Running

### 1. Navigate to Project Directory

If not already there, open your terminal and navigate to the project directory:
```bash
cd ResumeAnalyzer-main
```

### 2. Install Dependencies

Install the updated dependencies:
```bash
.venv\Scripts\pip install -r requirements.txt
```

### 3. Pre-download spaCy Language Model

To ensure the matching system works instantly, download the default English language model:
```bash
.venv\Scripts\python -m spacy download en_core_web_sm
```

### 4. Run the Application

Start the Streamlit application using the local environment:
```powershell
.venv\Scripts\streamlit run app.py
```

*Note: If you are already inside the `.venv/Scripts` folder, you can run:*
```powershell
.\streamlit run ..\..\app.py
```

---

## 👨‍💻 Author

**Biswajit Rout**

* GitHub: [@Biswa2531](https://github.com/Biswa2531)
* LinkedIn: [Biswajit Rout](https://linkedin.com/in/biswajitrout2526)

---

## 📄 License

This project is developed for **educational and academic purposes only**.
