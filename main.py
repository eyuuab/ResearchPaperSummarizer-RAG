import fitz
import os

def extract_text(path):
    pdf = fitz.open(path)
    text = ''
    for page in pdf:
        text +=page.get_text()
    return text

def extract_text_from_directory(directory):
    text = {}
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            path = os.path.join(directory, file)
            text[file] = extract_text(path)
    return text

directory = 'data'
extracted_text = extract_text_from_directory(directory)


