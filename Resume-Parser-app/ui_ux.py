
import gradio as gr
from CV_Parser import *

def process_cvs(files):
    results = []
    for file in files:
        try:
            # Since `file` is a bytes object, derive the extension from the file types allowed
            # In this case, we assume all files are either .pdf or .docx
            if file[:4] == b"%PDF":
                file_extension = ".pdf"
            elif file[:2] == b"PK":  # DOCX files start with "PK" in binary
                file_extension = ".docx"
            else:
                raise ValueError("Unsupported file format")
            
            parsed_data = parse_resume(file, file_extension)
            results.append(parsed_data)
        except Exception as e:
            results.append({"error": str(e)})
    return json.dumps(results, indent=4)

# Create Gradio interface
with gr.Blocks() as app:
    gr.Markdown("### Resume Parser")
    gr.Markdown("Drag and drop multiple CVs (PDFs or Word documents) to extract structured data.")
    
    # Update the file input type
    file_input = gr.File(label="Upload CVs", type="binary", file_types=[".pdf", ".docx"], file_count="multiple")
    output = gr.JSON(label="Parsed Resumes")
    
    submit_btn = gr.Button("Parse Resumes")
    submit_btn.click(fn=process_cvs, inputs=file_input, outputs=output)

if __name__ == "__main__":
    app.launch()