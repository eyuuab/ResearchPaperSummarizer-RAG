import os
import string
import nltk

nltk.download('punkt_tab')

def process_text(text):
    cleaned_text = text.replace('\n', ' ').strip()
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(cleaned_text)
    return ' '.join(tokens)


    pass
directory = 'data'
input_file_path = os.path.join(directory, 'extracted_text.txt')

with open(input_file_path, 'r') as file:
    extracted_text = file.read()

processed_text = process_text(extracted_text)

output_file_path = os.path.join(directory, 'processed_text.txt')
with open(output_file_path, 'w') as file:
    file.write(processed_text)