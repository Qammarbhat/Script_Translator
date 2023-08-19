from docx import Document

# text = ""
def docx_parser(script):
    text = ""
    document = Document(script)
    for para in document.paragraphs:
        text += para.text + "\n"
    return text