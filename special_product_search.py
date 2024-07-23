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
        [f"Name: {p['name']}\nFeatures: {', '.join(p['features'])}\nBenefits: {', '.join(p['benefits'])}" for p in products]
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
        f"2. automotive: Products related to vehicles, including electric motors, batteries, and other automotive components.\n\n"
        f"Based on the user query, determine which category (Solar Photovoltaics or Automotive) best matches the query. Provide only the category name and it should be all in lower case letters."
    )

    category = openai_call(category_prompt)

    recommendation = openai_call(generate_openai_prompt(user_query, get_products_by_category(category)))

    return recommendation

if __name__ == "__main__":
    user_query = "For my solar panel plant, I need to be able to to measure the temprature in my Thin Film Deposition machine. What do I need for that? What product would you recommend?"
    print(search_special_product(user_query))
