import os
from CV_Data_Extractor import *
import json 

def parse_resume(file_content, file_extension):
    
    file_text = extract_text_from_file(file_content, file_extension)
    file_text = data_preprocessing(file_text)
    if not file_text:
        raise ValueError("Failed to extract text from the resume file")
    
    system1_prompt = f""" 
        Extract the following information from a CV/Resume text 
        Output strictly in JSON format. Do not include any additional text, comments, or explanations outside of the JSON camelCase structure.

        -fullName
        -email
        -phoneNumber
        -address (including street, postalCode, country, and city)
        -experience of most recent 2 jobs only (jobTitle, company, duration)
        -currentJobTitle (if available, otherwise extract from the most recent job experience's job title; if both are unavailable, set to null)
        -education: most recent 2 qualifications only (degree, institution, graduationYear) 
            - Include degrees such as University degree (Bachelor's), Master's, PhD, A-level, GCSE/O-level, diploma, or other certifications
            - If degree information is not available, extract from the most recent education entry
            - If both qualifications are unavailable, set degree, institution, and graduationYear to null
        -domainAndField of candidate (analyze the content of the CV and extract the domain and field of the candidate)
        
        -Additional Instructions:
        -Please do not give Here is the extracted information in JSON format using camelCase just return json result in the answer.
        -Prioritize extracting the currentJobTitle and domainAndField of the candidate.
        """

    chat_completion = client.chat.completions.create(
    
        messages=[
        
            {
                "role": "system",
                "content": system1_prompt
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": file_text,
            }
        ],

        model="llama3-8b-8192",
        temperature=0,
        max_tokens=2048,
        top_p=1,
        stop=None,
        stream=False,
        seed= 12345   
    )

    # Print the completion returned by the LLM.
    model_output = chat_completion.choices[0].message.content

    if not model_output:
        raise ValueError("Model output is empty")
    
    parsed_resume = json.loads(model_output)

    # Return the JSON serialized string
    return json.dumps(parsed_resume, indent=4)

