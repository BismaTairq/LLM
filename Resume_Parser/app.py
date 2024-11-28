from flask import Flask, request, jsonify, send_file, Response
from CV_Data_Extractor import *
from Resume_Parser import *
import json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app,origins="*")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    file_extension = os.path.splitext(filename)[1].lower()
    file_content = file.read()
    # print(file_content)

    if file_extension in ['.pdf', '.docx', '.doc']:
        parsed_resume = parse_resume(file_content, file_extension)
        text = extract_text_from_file(file_content, file_extension)
        text = data_preprocessing(text)
        return jsonify({"parsed_resume": json.loads(parsed_resume), "processed_text": text}), 200
    else:
        return jsonify({"error": "Invalid file type, only PDF, DOCX, and DOC are allowed"}), 400
    
if __name__ == '__main__':
    app.run(port=8000, debug=True, threaded=True)

