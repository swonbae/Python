#! python3
# from 'https://automatetheboringstuff.com/'

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(' '+para.text)
    return '\n\n'.join(fullText)