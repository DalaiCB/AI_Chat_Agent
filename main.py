from icecream import ic
from langchain.prompts import ChatPromptTemplate
import os
import csv

from llama_requests import llama
from gpt_extract_name import name_extracter
from query_interpreter import query_interpretation
from product_rec import search_products
from get_name import search_product_files
from general_llama import general_request
from list_models import list_models_check, show_models


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
    
    ic(multiple_products)

    # Search for the last product name saved for the session ID
    name_in_memory = SessionManager().search_session(session_id)
    
    # If product name is not found, use last product name saved in memory.
    if extracted_product_names is None:
        if name_in_memory is None:
            return "Product name not found in query."
        else:
            extracted_product_names = []

            if " ~~ " in name_in_memory:
                extracted_product_names = name_in_memory.split(" ~~ ")
            else:
                extracted_product_names.append(name_in_memory)
    elif len(extracted_product_names) >= 3:
        return "The model can only handle up to 2 product names at a time. Please specify fewer products."
    elif len(extracted_product_names) == 1:
        product_name = ''.join(extracted_product_names)
        SessionManager().save_session(session_id, product_name)
    elif len(extracted_product_names) > 1:
        multiple_product_names = " ~~ ".join(extracted_product_names)
        SessionManager().save_session(session_id, multiple_product_names)

    return llama(user_query, get_datasheets(extracted_product_names)), extracted_product_names


# Main function to handle the user query and return the agent response
def main(raw_user_query, session_id):
    ERROR_MESSAGE = "There was an issue with the model. Please try again."
    log_line = "----------------------------------------------------"

    # Process the raw user query text
    user_query = process_raw_query(raw_user_query)

    list_models_only = list_models_check(user_query)
    ic(list_models_only)
    if list_models_only:
        series_name, multiple_products = name_extracter(user_query)

        series_name_str = str(series_name[0])
        
        models = show_models(series_name_str)
        model_list = ', '.join(models)

        if model_list:
            return f"All the models for {series_name_str} are {model_list}."
        else:
            return f"Models for {series_name_str} was not found."
        
        
    
    user_query_interp = query_interpretation(user_query)

    ic(user_query_interp)
    
    # Check if the user query is a product recommendation query
    try:        
        if user_query_interp == "Llama":
            return general_request(user_query)
        
        if user_query_interp == "Product recommendation":            
            recommended_products = search_products(user_query, disable_print=True)
            
            if isinstance(recommended_products, str) and recommended_products == "NO PRODUCTS FOUND":
                recommended_products = "No products found for the specified criteria."
            
            print(f"\n\n{log_line}\n{log_line}")
            print("\n\t\tUser Query:\n", user_query)
            print(f"\nInterpretation: {user_query_interp}")
            print("\n\t\tAgent Response:\n", recommended_products)
            
            return recommended_products
    except Exception as e:
        ic("\n\t\tError: Product recommendation failed.\n", e)
        
        return ERROR_MESSAGE

    # Regular search for product information
    try:
        agent_response, extracted_product_names = search(user_query, session_id)
    except Exception as e:
        ic("\n\t\tError: General search failed.\n", e)
        
        return ERROR_MESSAGE
    
    # LOGS
    print(f"\n\n{log_line}\n\t\tLOG\n{log_line}")
    print("\n\t\tUser Query:\n", user_query)
    print(f"\nInterpretation: {user_query_interp}")
    print("Extracted product Name:", extracted_product_names)
    print("\n\t\tAgent Response:\n", agent_response)
    print(f"\n\n{log_line}\n\t\tLOG\n{log_line}\n")
    
    return agent_response


if __name__ == "__main__":
    user_query = "What is the efficiency?"
    session_id = "290ceba4-b8ef-49b3-a869-f4d89d95c548"
    
    print("\n\t\tAgent Response:\n", main(user_query, session_id))
