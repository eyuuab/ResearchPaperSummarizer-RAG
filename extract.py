import fitz  # PyMuPDF
import os

def extract_text(path):
    pdf = fitz.open(path)
    text = ''
    for page in pdf:
        text += page.get_text()
    return text

def extract_text_from_directory(directory):
    text = ""
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            path = os.path.join(directory, file)
            text += extract_text(path)
            print(f"Extracted text from {file}")
    return text

if __name__ == "__main__":
    directory = 'data'  
    extracted_text = extract_text_from_directory(directory)
    
    output_file_path = os.path.join('data', 'extracted_text.txt')
    with open(output_file_path, 'w') as file:
        file.write(extracted_text)
    
    print(f"Text extraction completed and saved to {output_file_path}")
