import os
import sys
from openai import OpenAI


# Function to call the OpenAI API for query interpretation
def query_interpretation(query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    
    prompt = """
    Please provide a response based on the following query types:

    1. Product recommendation: If the query pertains to finding or recommending a product based on specific criteria, respond with "Product recommendation".
    2. None: If the query does not involve seeking a product recommendation, respond with "None".

    Examples of expected responses based on the queries are as follows:
        - Product recommendation: "I need a product with output current of 62.3 amps."
        - Product recommendation: "What products can output over 50A?"
        - Product recommendation: "I'm looking for a 1000W power supply with at least 2 years warranty."
        - None: "What is the output current of LCM300 series?"
        - None: "What is the operating temperature of LGA80D?"
        - None: "How efficient is the NGB1200?"
    
    Interpret the query: {}
    """
    
    # Call the OpenAI API to interpret the query
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt.format(query)}
        ], 
        max_tokens=50
    )
    
    message_content = response.choices[0].message.content.strip()

    return message_content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    query_interpretation(query)
