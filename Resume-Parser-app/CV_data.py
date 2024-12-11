import io
import re
import fitz  
import docx2txt

def extract_text_from_file(file_content, file_extension):
    """
    Extracts text from a file (either PDF, DOCX, or DOC) with support for conversion and processing.
    
    Parameters:
        file_content (bytes): The content of the file in binary format.
        file_extension (str): The file extension (e.g., '.pdf', '.doc').
        
    Returns:
        str: Extracted text from the file.
    """
    combined_text = ""
    
    if file_extension == '.pdf':
        try:
            # Load PDF content from bytes
            pdf_document = fitz.open("pdf", file_content)
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                combined_text += page.get_text()
        except Exception as e:
            print(f"An error occurred while extracting text from PDF: {str(e)}")

    elif file_extension == '.docx':
        try:
            file_like = io.BytesIO(file_content)
            text = docx2txt.process(file_like)
            word_count = len(text.split())
            combined_text = ' '.join(text.split()) 
        except Exception as e:
            print(f"An error occurred while extracting text from DOCX: {str(e)}")

    return combined_text

def data_preprocessing(text):
    """
    Cleans up and preprocesses extracted text.
    
    Parameters:
        text (str): Raw extracted text.
        
    Returns:
        str: Cleaned and preprocessed text.
    """
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'\r\r|\r', ' ', text)
    return text