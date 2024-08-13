from icecream import ic
from langchain.prompts import ChatPromptTemplate
from openai import OpenAI
import os
import csv

from llama_requests import llama
from gpt_extract_name import name_extracter
from query_interpreter import query_interpretation
from product_rec import search_products
from get_name import search_product_files
from general_llama import general_request
from list_models import list_models_check, show_models
from openai_api import openai_call
from special_product_search import search_special_product


# Class to manage user sessions and save product names
class SessionManager:
    # Initialize the SessionManager with the file path for saving sessions
    def __init__(self, file_path='sessions.csv'):
        self.file_path = file_path
        self.sessions = self.load_sessions()

    # Load session data from the CSV file
    def load_sessions(self):
        sessions = {}
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    session_id = row['session_id']
                    sessions[session_id] = [value for key, value in row.items() if key != 'session_id']
        return sessions

    # Save session data to the CSV file
    def save_sessions(self):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['session_id'] + [f'product_{i}' for i in range(1, len(max(self.sessions.values(), key=len)) + 1)]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for session_id, products in self.sessions.items():
                row = {'session_id': session_id}
                for i, product in enumerate(products, start=1):
                    row[f'product_{i}'] = product
                writer.writerow(row)

    # Save the product name for a given session ID
    def save_session(self, session_id, name):
        if session_id in self.sessions:
            last_names = self.sessions[session_id]
            
            if last_names and last_names[-1] == name:
                print(f"Skipping saving {name} for Session ID {session_id} since it's the same as the last name.")
                return
            
            # Ensure maximum of 4 products
            if len(last_names) >= 4:
                del last_names[0]  # Remove the oldest product (product_1)
            
            # Fill in blank entries for unmentioned products
            last_names.extend([''] * (4 - len(last_names)))  # Fill in blanks if less than 4 products
        else:
            last_names = [''] * 4  # Initialize to 4 blank products
    
        last_names[-1] = name  # Save the new name as the last product
        self.sessions[session_id] = last_names
        self.save_sessions()

    # Search for the last product name saved for a given session ID
    def search_session(self, session_id):
        # Check if the session ID exists in the sessions
        if session_id in self.sessions:
            products = self.sessions[session_id]
            last_product = products[-1] if products else None
            
            # Check if the last product name is not empty
            if last_product:
                print(f"Session ID: {session_id} Found\nLast Product Name: {last_product}")
                return last_product
            else:
                print(f"No product names found for Session ID: {session_id}")
                return None
        else:
            print(f"Session ID {session_id} not found.")
            return None


# Function to process the raw query text
def process_raw_query(raw_query):
    raw_query = raw_query.replace('"', '\\"')
    # Split the string into words and remove any empty
    words = raw_query.split()
    # Join the words back together with a single space between them
    processed_query_text = " ".join(words)
    return processed_query_text


# Function to get the file path for the datasheet of a product
def datasheet_file_path(product_name):
    datasheets_dir = "data/test_md"
    
    matching_files = search_product_files(product_name)

    md_file = matching_files[0]

    return os.path.join(datasheets_dir, md_file)


# Function to read the datasheet content from a file
def read_datasheet_from_file(product_name):
    datasheet_path = datasheet_file_path(product_name)
    
    print("Datasheet Path:", datasheet_path)

    if os.path.exists(datasheet_path):
        with open(datasheet_path, "r") as file:
            datasheet_content = file.read()
            return datasheet_content
    else:
        print("\n\nDatasheet not found for", product_name, "\n\n")
        return f"Datasheet not found for {product_name}."


# Function to combine the datasheets of multiple products
def get_datasheets(extracted_product_names):
    combined_datasheet_content = ""
    separator = "\n##########\n"

    for i, product_name in enumerate(extracted_product_names):
        datasheet_content = read_datasheet_from_file(product_name)
        
        if i > 0:
            combined_datasheet_content += separator
        
        combined_datasheet_content += datasheet_content

    return combined_datasheet_content


# Function to search for the product name in the user query and retrieve the datasheet content
def search(user_query, session_id):
    # Extract the product name from the user query
    extracted_product_names, multiple_products = name_extracter(user_query)
    
    print(f"\nExtracted Product Names: {extracted_product_names}")
    print(f"Multiple Products: {multiple_products}\n")

    # Search for the last product name saved for the session ID
    name_in_memory = SessionManager().search_session(session_id)
    
    # If product name is not found, use last product name saved in memory.
    if extracted_product_names is None:
        ic()
        if name_in_memory is None:
            ic()
            return "Product name not found in query.", ''
        else:
            ic()
            extracted_product_names = []

            if " ~~ " in name_in_memory:
                extracted_product_names = name_in_memory.split(" ~~ ")
            else:
                extracted_product_names.append(name_in_memory)
    elif len(extracted_product_names) >= 3:
        ic()
        return "The model can only handle up to 2 product names at a time. Please specify fewer products."
    elif len(extracted_product_names) == 1:
        ic()
        product_name = ''.join(extracted_product_names)
        SessionManager().save_session(session_id, product_name)
    elif len(extracted_product_names) > 1:
        ic()
        multiple_product_names = " ~~ ".join(extracted_product_names)
        SessionManager().save_session(session_id, multiple_product_names)

    return llama(user_query, get_datasheets(extracted_product_names)), extracted_product_names



# Main function to handle the user query and return the agent response
def main(raw_user_query, session_id):
    ERROR_MESSAGE = "There was an issue with the model. Please try again."

    # Process the raw user query text
    user_query = process_raw_query(raw_user_query)
    user_query_interp = query_interpretation(user_query)

    print("\n\nUser Query:", user_query)
    print("User Query Interpretation:", user_query_interp)
    
    # Check if the user query is a product recommendation query
    try:
        list_models_only = list_models_check(user_query)
        print("\n\nList Models:", list_models_only)

        if list_models_only:
            series_name, multiple_products = name_extracter(user_query)
            models = show_models(series_name)
            model_list = ', '.join(models)

            return f"All the models for {series_name} are {model_list}."
        
        if user_query_interp == "Llama":
            return general_request(user_query)

        if user_query_interp == "Product recommendation":            
            special_case_prompt = (
                    f"User query: \"{user_query}\"\n\n"
                    f"Based on the user query, determine if the query is related to solar photovoltaics, automotive, Magnetic resonance imaging (MRI), RF electrosurgery devices, and laser products (CNC machines, etc) products. If the query is related to any of these, return True. Otherwise, return False. Only respond with 'True' or 'False'."
                )
            openai_response = openai_call(special_case_prompt)
            special_case = eval(openai_response)

            try:
                if special_case:
                    return search_special_product(user_query)
            except Exception as e:
                print("\n\t\tError: Special product search failed.\n", e)
                
                return ERROR_MESSAGE

            recommended_products = search_products(user_query, disable_print=True)
            
            if isinstance(recommended_products, str) and recommended_products == "NO PRODUCTS FOUND":
                recommended_products = "No products found for the specified criteria."
            
            return recommended_products

    except Exception as e:
        print("\n\t\tError: main()\n", e)
        
        return ERROR_MESSAGE

    # Regular search for product information
    try:
        ic()
        agent_response, extracted_product_names = search(user_query, session_id)
        print("\n\n\t\tProduct Names:", extracted_product_names)
    except Exception as e:
        print("\n\t\tError: General search failed.\n", e)
        return ERROR_MESSAGE
    
    return agent_response


if __name__ == "__main__":
    user_query = 'What is the MTBF of the lpt100?'
    session_id = "290ceba4-b8ef-49b3-a869-f4d89d95c548"
    agent_response = main(user_query, session_id)
    print("\n\t\tAgent Response:\n", agent_response)
    #print(type(agent_response))
