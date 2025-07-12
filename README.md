# 🤖 AI-Powered Recruitment Toolkit (LLM-Based Solutions)

This repository showcases a suite of AI-powered tools designed to streamline and enhance the recruitment process. Built using cutting-edge machine learning and language model techniques, this package includes:

- A Job Description to Resume Matching System
- A Resume Parsing Application
- A Webpage Summarizer powered by LLMs

---

## 📌 1. CV-JD Matcher

An intelligent system that automatically matches resumes with job descriptions using machine learning, helping recruiters efficiently identify the best candidates.

### 🚀 Features

- **Job Description Input**: Recruiters can input job descriptions into the system.
- **Resume Upload**: Candidates can upload resumes for automatic matching.
- **Matching Algorithm**: Uses ML models to score resume relevance based on job requirements.
- **Results View**: Displays matched resumes with similarity scores and relevant details.

### 🛠️ Technologies Used

- `Python`: Backend development
- `Flask`: Web server and routing
- `Bootstrap`: Frontend design
- `scikit-learn`: Machine learning for similarity matching
- `HTML/CSS`: UI development

---

## 📌 2. Resume Parser App

A web-based application that parses multiple resumes and extracts structured information such as skills, experience, and education.

### 🚀 Features

- Upload multiple resumes (`PDF`, `DOCX`)
- Extracts fields:
  - Full Name
  - Email
  - Phone Number
  - Address
  - Experience
  - Education
  - Skills
  - Certifications (optional)
  - Domain & Field
- JSON output for integration with other systems
- Data saved to a PostgreSQL database
- User-friendly interface using Gradio

### 🛠️ Technologies Used

- `Python`
- `Gradio`
- `PostgreSQL`
- `Resume Parsing Libraries` (e.g., SpaCy, custom NER models)

---

## 📌 3. Summarize Webpage via Ollama

A minimal AI demo using the Ollama API to summarize any public webpage into a short, readable summary.

### 🚀 Features

- **Webpage Summarization**: Input a URL, and get a summarized version of the page.
- **AI-Powered**: Utilizes the Ollama LLM API for accurate summarization.
- **Notebook-Based**: Easily test and run inside a Jupyter environment.

### 🧪 Usage

1. Open `summarize_webpage.ipynb` in Jupyter Notebook.
2. Input the target URL.
3. Run the notebook to fetch and summarize the content.
4. Output appears in a readable text block.

---

## 💼 Use Case

This toolkit is ideal for:
- HR teams and recruiters automating resume screening
- ATS and HR software vendors looking to integrate smart matching/parsing
- Data science teams building custom NLP-based hiring workflows

---

## 🧩 Future Enhancements

- Add support for real-time resume parsing via API
- Improve JD-Resume matching with Transformer-based embeddings
- Add LLM fine-tuning capability for domain-specific recruitment

---

## 📬 Contact

For questions, collaboration, or contributions, feel free to reach out or open an issue.

---

## 📄 License

This project is licensed under the MIT License.
