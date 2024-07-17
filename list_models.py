import os
import re
import pandas as pd
from icecream import ic
from openai import OpenAI

def list_models_check(user_query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    
    prompt = """
    Please analyze the following user query and determine if the user is asking for part numbers or model numbers related to a specific series of products. 
    If the query is asking for such information, respond with "True". If the query does not match this pattern, respond with "False".

    Examples for "True":
    1. "What are the models of LGA80?"
    2. "Can you give me the part number for LCM300 series?"
    3. "Please show me all the models of NGB60."

    Examples for "False":
    1. "What is the warranty period for NGB60?"
    2. "How efficient is the LGA80D?"
    3. "What is the output current of LCM300?"
    4. "What is LCM300?"
    5. "What is LGA80D?"

    User Query: {}
    Assistant:
    """

    # Call the OpenAI API to interpret the query
    openai_response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt.format(user_query)}
        ], 
        max_tokens=50
    )
    
    openai_message_content = openai_response.choices[0].message.content.strip()

    if openai_message_content.startswith("True"):
        return True
    else:
        return False

def normalize_string(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def show_models(series_name):
    df = pd.read_csv('data/2.csv')
    
    try:
        normalized_series_name = normalize_string(series_name)
        
        df['Normalized_SeriesName'] = df.iloc[:, 1].astype(str).apply(normalize_string)
    
        matching_rows = df[df['Normalized_SeriesName'] == normalized_series_name]
    except Exception as e:
        ic(f"show_model error: {e}")
        return []

    ic("Series name:", series_name)
    ic(matching_rows)
    
    return matching_rows.iloc[:, 0].tolist()

if __name__ == "__main__":
    user_query = "What is the transient response of CoolX600?"
    series_name = "LCM300"

    #print(list_models_check(user_query))
    models = show_models(series_name)
    model_list = ', '.join(models)

    print(f"All the models for {series_name} are {model_list}.")
