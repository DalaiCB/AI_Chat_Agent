import os
from openai import OpenAI

def name_extracter(user_query):
    client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # System prompt. Query processing instructions for the AI assistant
    sys_prompt = """
    You are an assistant that extracts product names from user queries.
    If the query contains more than one product name, provide all the names separated by double tilde '~~'.
    Some product names may contain '-', '/', or other special characters. Please include them as well.
    If no product name is found, return None.

    Special Instructions: If the query contains Evergreen Vento or something similar, please return FCM10K as it is the same product.
    """

    prompt = f"Query: {user_query}"

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

    return message_content, multiple_products

if __name__ == "__main__":
    query = "What are the temperature ranges of IGA6/23?"

    print(name_extracter(query))
