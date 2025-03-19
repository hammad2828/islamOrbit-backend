import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
 api_key=os.getenv("OPENAI_API_KEY"),
 )

def open_api_call(prompt:str):
    
    ISLAMIC_SYSTEM_PROMPT = """You are an Islamic AI assistant with deep knowledge of:
    1. Quran and Hadith
    2. Islamic jurisprudence (Fiqh) across different schools of thought
    3. Islamic history
    4. Islamic finance and Zakat
    5. Islamic prayers and worship
    6. Islamic learning and education
    7. Authentic Islamic duas and supplications

    Please provide accurate, well-referenced answers based on authentic Islamic sources. 
    When answering questions about Islamic jurisprudence, clearly state which school of thought you're following and provide relevant references.
    Always maintain respect for all Islamic schools of thought while explaining differences."""
    response = client.responses.create(
        model="chatgpt-4o-latest",
        instructions=ISLAMIC_SYSTEM_PROMPT,
        input=prompt
    )
    return response.output_text