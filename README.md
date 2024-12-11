# LLM 
# 1. Resume Parser App
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
  
# 2. Summarize Webpage via Ollama
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
