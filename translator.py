from langchain import PromptTemplate
import os
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "Your API KAY"

# creating LLM (will try OpenAI, modelname= gpt-3.5-turbo)
llm = OpenAI(model_name = "gpt-3.5-turbo")

def text_translator(input_text, input_target_language, input_country_names):
    translate_prompt = PromptTemplate(
    input_variables = ["input_text", "target_language", "country_names"],
    template = """
    You are an advanced translator specializing in localizing scripts. Your task is to translate the following script into {target_language} while replacing any names with culturally appropriate names for {country_names}. Make sure to maintain the context and tone of the script.

    Here is the script for localization:

    {input_text}

    As you replace names, consider the cultural and linguistic context of {country_names}. Deliver a translation that resonates with the audience in {country_names}.
    """
    )
    # translated_text = llm(translate_prompt.format(text = input_text, target_language = input_target_language))
    # using chunks (Ran into token length issue, max tokens = 4096)


    max_input_length = 4096 - len(translate_prompt.format(input_text="", target_language=input_target_language, country_names = input_country_names))
    
    translated_chunks = []
    start_idx = 0
    
    while start_idx < len(input_text):
        # Calculate end indexxc ofchunk
        end_idx = min(start_idx + max_input_length, len(input_text))
        
        # chunk of input text
        chunk = input_text[start_idx:end_idx]
        
        # translating chunks that i generated above
        translated_chunk = llm(translate_prompt.format(input_text=chunk, target_language=input_target_language, country_names = input_country_names))
        
        # Appending translTEd chunk into list
        translated_chunks.append(translated_chunk)
        
        # Moving to next index
        start_idx = end_idx
    
    # joining translated chunks to get completee text
    translated_text = " ".join(translated_chunks)
    return translated_text