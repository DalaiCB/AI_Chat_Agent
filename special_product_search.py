import os
import json
from icecream import ic
from openai import OpenAI
from openai_api import openai_call

# Load your API key from an environment variable or directly set it here
client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

# Load the JSON data
with open('data/special_products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

def get_products_by_category(category):
    return products.get(category, [])

def generate_openai_prompt(user_query, products):
    product_info = "\n".join(
        [
            f"Name: {p.get('name', 'Unknown')}\n"
            + (
                f"Features: {', '.join(p.get('features', []))}\nBenefits: {', '.join(p.get('benefits', []))}"
                if 'features' in p and 'benefits' in p
                else f"Description: {p.get('description', 'No description available')}"
            )
            for p in products
        ]
    )
    prompt = f"User query: {user_query}\n\nProduct information:\n{product_info}\n\nBased on the above product information, provide a short and precise product recommendation and explain why. Don't include 'Recommendation', 'Reason', or 'Explanation' etc in your response."
    
    ic(prompt)
    
    return prompt


""" def openai_call(prompt):
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "user", "content": prompt}
        ], 
        max_tokens=300
    )

    return response.choices[0].message.content.strip() """

def search_special_product(user_query):
    category_prompt = (
        f"User query: \"{user_query}\"\n\n"
        f"Categories:\n"
        f"1. solar photovoltaics: Products related to solar energy systems and their components, including solar panels, inverters, and power supplies.\n"
        f"2. automotive: Products related to vehicles, including electric motors, batteries, and other automotive components.\n"
        f"3. mri: Products related to magnetic resonance imaging (MRI) machines and their components, including scanners, coils, and power supplies.\n"
        f"4. rf: Products related to RF electrosurgery devices and their components, including generators, electrodes, and power supplies.\n"
        f"5. lasers: Products related to laser systems and their components, including laser sources, optics, and power supplies.\n\n"
        f"Based on the user query, determine which category best matches the query. Provide only the category name and it should be all in lower case letters."
    )

    category = openai_call(category_prompt)

    recommendation = openai_call(generate_openai_prompt(user_query, get_products_by_category(category)))

    return recommendation

if __name__ == "__main__":
    user_query = "I manufacture CNC machines for small applications e.g. the development of small tools. I need a power supply that is affordable and reliable. Can you let me know what you think I will need in terms of power, and if you have any products that meet those requirements?"
    print(search_special_product(user_query))
