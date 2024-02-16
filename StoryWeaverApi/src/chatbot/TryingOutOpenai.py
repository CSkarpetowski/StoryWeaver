import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print(os.getenv('OPENAI_API_KEY'))
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is human life expectancy in the United States?"},
    ]
)
