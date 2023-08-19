from docx import Document

# Define a function to parse text from a DOCX document
def docx_parser(script):
    text = ""  # Initialize an empty string to store the parsed text
    document = Document(script)  # Load the provided DOCX document
    for para in document.paragraphs:
        text += para.text + "\n"  # Append each paragraph's text followed by a newline
    return text  # Return the parsed text as a single string
