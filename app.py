import streamlit as st
from io import BytesIO
from translator import text_translator
from docx import Document
from doc_reader import docx_parser

st.set_page_config(page_title="Script Translator", page_icon=":page_with_curl:")

st.title("Script Translator")

# Taking inputs from user
uploaded_file = st.file_uploader("Choose a docx file", type="docx")
target_language = st.selectbox("Select target language", ["English", "French", "Pirated English", "German"])
target_country = st.selectbox("Select target country", ["India", "United States", "Spain", "France", "Germany", "China"])

submit = st.button("Submit")

if uploaded_file is not None and submit:
    text = docx_parser(uploaded_file)
    st.header("Your Input Text")
    st.text(text)

    translated_text = text_translator(text, target_language, target_country)
    st.header("Your Translated Text")
    st.write(translated_text)

# Outputting in docx format
    output_doc = Document()
    output_doc.add_heading("Translated Text", level = 1)
    output_doc.add_paragraph(translated_text)
    output_doc_stream = BytesIO()
    output_doc.save(output_doc_stream)
    output_doc_stream.seek(0)

# Creatring Downloading link
    st.download_button(
        label="Download Translated Text (DOCX)",
        data=output_doc_stream,
        file_name="translated_text.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
