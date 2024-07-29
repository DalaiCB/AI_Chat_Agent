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
    3. Llama: If the query does not pertain to specific product recommendation but involves some other type of inquiry that doesn't directly relate to a specific product, respond with "Llama".

    Examples of expected responses based on the queries are as follows:
        - Product recommendation: "I need a product with output current of 62.3 amps."
        - Product recommendation: "What products can output over 50A?"
        - Product recommendation: "I'm looking for a 1000W power supply with at least 2 years warranty."
        - Product recommendation: "Do you have any units that will meet that power requirement?"
        - Product recommendation: "Let me know if you have any products that meet those requirements?"
        - None: "What is the output current of LCM300 series?"
        - None: "What is the operating temperature of LGA80D?"
        - None: "How efficient is the NGB1200?"
        - Llama: "How much power will I need?"
        - Llama: "What are my power requirements?"
        - Llama: "Can you help me figure out how much power I need?"

    Special instructions:
    - If the query has multiple questions, check if any of the questions are related to product recommendations. If any question is related to product recommendations, respond with "Product recommendation" and ignore the other questions.
    
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

    valid_responses = ["Product recommendation", "None", "Llama"]
    for valid_response in valid_responses:
        if message_content.startswith(valid_response):
            return valid_response

    # Default to "None" if no valid response is detected
    return "None"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    query_interpretation(query)
