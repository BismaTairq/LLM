import psycopg2
import json
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "host": os.getenv('DB_HOST'),
    "port": os.getenv('DB_PORT')
}

def connect_to_db():
    return psycopg2.connect(**DB_CONFIG)

def insert_into_database(parsed_resume):
    conn = None
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO parsed_resumes (
                full_name, email, phone_number, address, experience, 
                current_job_title, education, skills, certifications, domain_and_field
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            parsed_resume.get("fullName"),
            parsed_resume.get("email"),
            parsed_resume.get("phoneNumber"),
            json.dumps(parsed_resume.get("address")),
            json.dumps(parsed_resume.get("experience")),
            parsed_resume.get("currentJobTitle"),
            json.dumps(parsed_resume.get("education")),
            json.dumps(parsed_resume.get("skills")),
            json.dumps(parsed_resume.get("certifications")),
            json.dumps(parsed_resume.get("domainAndField"))
        ))
        
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
