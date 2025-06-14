import sys
import PIL.Image
import google.generativeai as genai
import json
import time
from dotenv import load_dotenv
import os


def generate_explanation_for_question(record, model, subject, code, level, image_path):
    """
    Generates an explanation for a single question record and appends it to the record.
    """
    file = record["questionName"]
    print(f"***************************{file}********************************")
    img = PIL.Image.open(f"{image_path}/{file}")
    answerGenerated = False
    response = None
    while not answerGenerated:
        try:
            response = model.generate_content([
                img,
                    f"""
                    Your task is to clearly explain why the answer {record["Answer"]} is correct and why each of the other options is incorrect.
                    Provide detailed yet concise explanations thorough enough that students fully understand the reasoning without needing additional resources.
                    Maintain a formal, textbook-style tone, clearly articulating scientific concepts and processes.
                    Do not refer to the image, question format, or directly address the student.
                    Structure each explanation logically and coherently, ensuring it stands fully on its own.

                    The subject is {subject}, curriculum {code}, and the level is {level}.

                    These explanations will appear beneath each question on an educational study website.
                    """], 
                safety_settings={
                    'HATE': 'BLOCK_NONE',
                    'HARASSMENT': 'BLOCK_NONE',
                    'SEXUAL': 'BLOCK_NONE',
                    'DANGEROUS': 'BLOCK_NONE'
                })
            if len(response.text) > 10:
                answerGenerated = True
        except Exception as e:
            print(f"""failed, trying again {record["questionName"]} error code: {e}""")
            time.sleep(0.5)
    record["Explanation"] = response.text
    print(response.text)

def generate_explanations_for_all_questions(json_name):
    """
    Generates explanations for all questions in the provided JSON file.
    
    Args:
        json_name (str): The name of the JSON file containing question data.
    
    """
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    json_path = os.path.join(base_dir, "resources", "json", json_name)
    question_data = json.load(open(json_path, "r"))
    subject = question_data[0]["Subject"]
    paper_number = question_data[0]["paperNumber"]
    code = question_data[0]["pdfName"].split("_")[0]
    level = question_data[0]["Level"]
    if level.lower() == "igcse":
        image_path = os.path.join(base_dir, "resources", "images", "questions", "igcse", subject, f"p{paper_number}")
    else:
        image_path = os.path.join(base_dir, "resources", "images", "questions", "a-level", subject, f"p{paper_number}")
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-pro-preview-06-05")
    print(question_data[0]["pdfName"].split("_")[0])
    try:
        for record in question_data:
            question_path = f"{image_path}/{record['Chapter']}"
            generate_explanation_for_question(record, model, subject, code, level, question_path)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Saving progress to JSON file...")
        json.dump(question_data, open(json_path, "w"))
        print(f"Progress saved to {json_path}")
        sys.exit(0)
    json.dump(question_data, open(json_path, "w"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python explanation_generator.py <json_file>")
        sys.exit(1)
    json_name = sys.argv[1]
    generate_explanations_for_all_questions(json_name)