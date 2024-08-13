import os
import sys
from openai import OpenAI


# Function to call the OpenAI API for query interpretation
def query_interpretation(query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    
    prompt = """
    Please classify the following query into one of the three categories:

    1. Product recommendation: For queries where the user is asking for recommendations or suggestions about products. This includes queries that mention power, current, or features as part of the search criteria but are focused on finding or recommending products.
    2. None: For queries focused on specific details, features, specifications, or benefits of one particular product or a specific product model. This includes questions about power, current, efficiency, temperature, and other technical specifications. Even follow-up questions that reference these details should be classified as "None."
    3. Llama:  For queries that do not ask for product recommendations and are not focused on specific technical details or features. These are often vague or broad questions where the user is not directly asking about a product or its specifications.

    Examples of expected responses based on the queries are as follows:
        - Product recommendation: "I need a product with output current of 62.3 amps."
        - Product recommendation: "What products can output over 50A?"
        - Product recommendation: "I'm looking for a 1000W power supply with at least 2 years warranty."
        - Product recommendation: "Do you have any units that will meet that power requirement?"
        - Product recommendation: "Let me know if you have any products that meet those requirements?"
        - None: "What is the output current of LCM300 series?"
        - None: "What is the operating temperature of LGA80D?"
        - None: "How efficient is the NGB1200?"
        - None: "What is the total power of ADQ700?"
        - None: "What is the power?"
        - None: "Give me the precision."
        - Llama: "How much power will I need?"
        - Llama: "What are my power requirements?"
        - Llama: "Can you help me figure out how much power I need?"

    Special instructions:
    - If the query has multiple questions, check if any of the questions are related to product recommendations. If any question is related to product recommendations, respond with "Product recommendation" and ignore the other questions.
    - Determine whether a query is a follow-up question or a new query. If it is likely a follow-up type question, classify it as "None". In doubt, classify it as "None".

    Given the query, provide only the appropriate category label ("Product recommendation," "None," or "Llama").

    Query: {}
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
    query = "What is the total power?"

    print(query_interpretation(query))
