import os
from openai import OpenAI

client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

def openai_call(prompt):
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "user", "content": prompt}
        ], 
        max_tokens=300
    )

    return response.choices[0].message.content.strip()