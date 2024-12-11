from flask import Flask, request, jsonify
from CV_data import *
from CV_Parser import *

app = Flask(__name__)

def is_html(text):
    return bool(re.search(r'<.*?>', text)) 

@app.route('/resume_parser', methods=['POST'])
def resume_parser():
    
    file = request.files['file']

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
        
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    file_extension = os.path.splitext(filename)[1].lower()
    file_content = file.read()

    if file_extension in ['.pdf', '.docx', '.doc']:
        parsed_resume = parse_resume(file_content, file_extension)
        resume_text = extract_text_from_file(file_content, file_extension)
        resume_text = data_preprocessing(resume_text)
    
    resume_output = json.loads(parsed_resume)
    return jsonify({
            "parsed_resume": resume_output, 
            "processed_text": resume_text,
    }), 200
    
    
if __name__ == '__main__':
    app.run(debug=True)

