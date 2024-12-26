# LLM 

# 1.CV-JD-Matcher

This project aims to build a job description and resume matching system using Python with machine learning techniques. The system helps streamline the recruitment process by automatically matching job descriptions with submitted resumes, providing recruiters with a more efficient way to identify suitable candidates.

## Features

- **Job Description Input:** Recruiters can input job descriptions into the system.
- **Resume Upload:** Candidates can upload their resumes for matching against job descriptions.
- **Matching Algorithm:** The system utilizes machine learning algorithms to match job descriptions with resumes based on similarity scores.
- **Result Presentation:** Matched resumes are presented to recruiters with similarity scores and relevant details.

## Technologies Used

- **Python:** Backend development using Python programming language.
- **Flask:** Web framework for building the backend server and handling HTTP requests.
- **Bootstrap:** Frontend design and layout using Bootstrap for responsive and user-friendly UI.
- **Machine Learning Libraries:** Libraries such as scikit-learn for implementing machine learning algorithms for text similarity matching.
- **HTML/CSS:** Frontend markup and styling for web pages.

# 2. Resume Parser App
The Resume Parser App is a web-based application that allows users to upload multiple resumes (PDF or DOCX format) and extract structured information like personal details, experience, education, skills, and more using AI-based models.

## Features
- Upload multiple resumes (PDF and DOCX formats).
- Extract structured information: Full Name, Email, Phone Number, Address, Experience, Education, Skills, Certifications (optional), Domain, and Field.
- JSON output for easy integration with databases or other systems.
- Built with Gradio for an interactive web interface.

## Usage
- Upload multiple resumes (PDF or DOCX format).
- The app will parse each resume and extract structured information.
- View the parsed data in a JSON format.
- The data is stored in database (using PostgreSQL in this project).
  
# 3. Summarize Webpage via Ollama
Summarize Webpage via Ollama is a simple example of using the Ollama API to summarize the content of a webpage. By providing a URL, the notebook fetches the webpage content and generates a concise summary using AI-powered summarization.

## Features
- Summarize Webpages: Provide a URL, and the notebook fetches and summarizes the page.
- AI-Powered: Utilizes Ollama to process and summarize text content.
- Example Notebook: A quick, easy-to-run Jupyter notebook for experimenting with webpage summarization.

## Usage
- Open the summarize_webpage.ipynb notebook in Jupyter or any compatible notebook environment.
- Input the desired URL in the designated cell.
- Run the notebook. The app will fetch the webpage content and summarize it using Ollama.
- View the summarized content displayed in the output cell.
