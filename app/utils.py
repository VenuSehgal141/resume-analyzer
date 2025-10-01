import PyPDF2
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def parse_cv(file):
    cv_text = ""
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    for page_number in range(total_pages):
        page = reader.pages[page_number]
        cv_text += page.extract_text() + " "
    return cv_text

def get_analysis(model, messages, temperature, max_tokens):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content
