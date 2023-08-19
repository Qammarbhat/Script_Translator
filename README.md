# Script Translator Web App

The Script Translator Web App is a simple web application built using Streamlit that allows users to upload a DOCX file containing a script, select a target language and country, and receive a translated version of the script. The translation is generated using the OpenAI GPT-3.5 Turbo model and includes localized names from the selected country.

## Features

- Upload a DOCX file containing a script.
- Select a target language for translation.
- Choose a target country for localized names.
- Receive a translated version of the script with localized names.

## Installation

1. **Clone Repository**: Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/script-translator-web-app.git
    cd script-translator-web-app
    ```

2. **Install Dependencies**: Install the required packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key**: Open the `translator.py` file and replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key.

## Usage

1. **Run the App**: Launch the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. **Access the Web App**: Open your web browser and navigate to `http://localhost:8501` or the localhot address you get on your terminal.

3. **Upload and Translate**: Follow these steps on the web app:

    - Upload a DOCX file.
    - Select a target language.
    - Choose a target country for localized names.
    - Click the "Submit" button to generate the translated and localized script.

4. **Download Translated Script**: You can download the translated script in DOCX format using the provided download link.

## Project Structure

- `app.py`: Main Streamlit web application script.
- `translator.py`: Translation logic using the OpenAI GPT-3.5 Turbo model.
- `doc_reader.py`: Utility script to parse text from DOCX files.
- `requirements.txt`: List of required packages for the project.

## Contributing

Contributions are welcome! If you'd like to contribute to this project contact me.

## Contact

If you have any questions or feedback, feel free to contact me:

- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/qammarbhat/)
- **Email**: qammarbhat@bgsbu.ac.in

