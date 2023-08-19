from langchain import PromptTemplate
import os
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = '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'

# creating LLM (will try OpenAI, modelname= gpt-3.5-turbo)
llm = OpenAI(model_name = "gpt-3.5-turbo")

def text_translator(input_text, input_target_language, input_country_names):
    translate_prompt = PromptTemplate(
        input_variables = ["input_text", "target_language", "country_names"],
        template = """"
        You are a helpful Translator. Translate the following demo script into {target_language} and use names from {country_names}:
        {input_text}
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