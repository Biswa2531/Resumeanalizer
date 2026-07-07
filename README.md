# 📄 AI Resume Analyzer

<p align="center">
  <b>ATS Resume Analysis Tool using Python & Streamlit</b><br>Analyse resumes against job descriptions by matching skills and generating an ATS compatibility score.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/PyMuPDF-PDF%20Parser-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-Educational-blueviolet?style=for-the-badge">
</p>

---

# 📖 Overview

AI Resume Analyser is a web application built using **Python** and **Streamlit** that evaluates how well a resume matches a job description. The application extracts text from uploaded PDF resumes, identifies technical skills, compares them with the required skills in a job description, and generates an ATS (Applicant Tracking System) match score.

This project helps students and job seekers understand how closely their resumes align with job requirements and highlights skills that may need improvement.

---

# 🎯 Objectives

* Analyse resumes automatically.
* Compare resumes with job descriptions.
* Calculate an ATS match percentage.
* Identify matching and missing skills.
* Provide suggestions to improve resumes.
* Demonstrate PDF processing and text analysis using Python.

---

# ✨ Features

* 📄 Upload Resume (PDF)
* 📝 Enter Job Description
* 🔍 Automatic Skill Extraction
* 📊 ATS Match Score
* ✅ Matched Skills
* ❌ Missing Skills
* 💡 Resume Improvement Suggestions
* 🎨 Simple Streamlit Interface

---

# 🛠 Technology Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Programming Language      |
| Streamlit           | Web Application Framework |
| PyMuPDF (fitz)      | PDF Text Extraction       |
| Python Lists & Sets | Skill Matching            |
| VS Code             | Development Environment   |

---

# 💻 System Requirements

* Python 3.9 or above
* Streamlit
* PyMuPDF
* Windows/Linux/macOS
* Visual Studio Code (Recommended)

---

# 📂 Project Structure

```text
ResumeAnalyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── assets/
    └── screenshots/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Biswa2531/AI-Resume-Analyzer.git
```

```bash
cd AI-Resume-Analyzer
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the Application

```bash
streamlit run app.py
```

---

# 🚀 How to Use

1. Launch the Streamlit application.
2. Upload your resume in PDF format.
3. Paste the job description into the text box.
4. Click Analyse** Resume**.
5. View the ATS Match Score.
6. Review matched skills, missing skills, and improvement suggestions.

---

# 🔄 Workflow

```text
Upload Resume (PDF)
        │
        ▼
Extract Resume Text
        │
        ▼
Extract Skills
        │
        ▼
Enter Job Description
        │
        ▼
Extract Required Skills
        │
        ▼
Compare Skills
        │
        ▼
Calculate ATS Score
        │
        ▼
Display Report
```

---

# 📊 Analysis Report

The application provides:

* ATS Match Percentage
* Matched Skills
* Missing Skills
* Resume Improvement Suggestions

---

# 📸 Screenshots

Create a folder named **screenshots** and add application screenshots.

```text
screenshots/
│
├── home.png
├── upload.png
├── analysis.png
└── report.png
```

---

# 🌟 Key Highlights

* ATS Resume Evaluation
* Skill Extraction
* PDF Text Parsing
* Resume vs Job Description Comparison
* Match Percentage Calculation
* Interactive Streamlit Interface
* Beginner-Friendly Python Project

---

# 🔒 Validation

* Accepts only PDF resumes.
* Ensures a job description is provided before analysis.
* Prevents empty submissions.
* Displays warnings for invalid input.

---

# 🚀 Future Enhancements

* AI-powered resume suggestions using LLMs.
* Keyword ranking.
* Resume formatting analysis.
* Multiple resume comparisons.
* Export analysis report as PDF.
* Resume scoring based on experience and education.
* User authentication.
* Database integration.
* Cloud deployment.

---

# 🎓 Learning Outcomes

This project demonstrates:

* Python Programming
* Streamlit Application Development
* PDF Processing
* Text Extraction
* Skill Matching Algorithms
* Set Operations
* User Interface Design
* ATS Resume Analysis Concepts

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

# 👨‍💻 Author

**Biswajit Rout**

**MCA Student | Python & Full Stack Developer**

GitHub: https://github.com/Biswa2531

LinkedIn: https://linkedin.com/in/biswajitrout2526
---

# 📄 License

This project is developed for **educational and academic purposes only**.

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ ****star** on GitHub.
