import os
from openai import OpenAI

def name_extracter(user_query):
    client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
    )

    with open('data/names.txt', 'r') as file:
        product_names = file.read().splitlines()

    # System prompt. Query processing instructions for the AI assistant
    sys_prompt = """
    You are a helpful assistant that matches user queries to a list of product names. Given the list of product names below, find the best match for the user's query.
    If there are no matching products, simply return None.
    """

    prompt = f"Product Names:\n{', '.join(product_names)}\n\nUser Query: {user_query}\n\nReturn only the full name of the matching product or None if unable to match to a name."

    # Call the OpenAI API to process the user query
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ], 
        max_tokens=50
    )

    stripped_response = response.choices[0].message.content.strip()

    if "~~" in stripped_response:
        multiple_products = True
        message_content = stripped_response.split("~~")
    elif "None" in stripped_response:
        return None, False
    else:
        message_content = [stripped_response]
        multiple_products = False

    print(f"GPT Extract Name: {message_content}\nMultiple Name: {multiple_products}.")
    
    return message_content, multiple_products

if __name__ == "__main__":
    query = "What are the temperature ranges of IGA6/23?"

    print(name_extracter(query))
