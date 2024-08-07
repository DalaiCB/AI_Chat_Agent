from langchain.prompts import ChatPromptTemplate
from icecream import ic
import requests

from process_llama_response import process


API_URL = "https://bo1zekebo4gy1v0e.us-east-1.aws.endpoints.huggingface.cloud"
HEADERS = {
	"Accept" : "application/json",
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

CHROMA_PATH = "chroma_test"
PROMPT_TEMPLATE = """
{context}\n\n
Based on the this information, provide a short and precise answer for the following question: {question}

Note: Please add "~~~" at the end of each answer.

Assistant:
"""


# Function to format and extract the response from the Llama API
def format_response(llama_response):
    if isinstance(llama_response, list) and len(llama_response) > 0:
        # Extract the text from the "generated_text" key in the first dictionary
        response_text = llama_response[0].get('generated_text', '')
        
        # Find the index of "Assistant:"
        assistant_index = response_text.find("Assistant:")
        
        # If "Assistant:" is found, extract the text before it
        if assistant_index != -1:
            return response_text[:assistant_index].strip()
        
        # If "Assistant:" is not found, return the entire response text
        return response_text.strip()
    
    # If the input is not a valid list, return None
    return None


# Function to send a request to the Llama API
def send_request(user_query, datasheet_content):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=datasheet_content, question=user_query)
    #print("\n\n\t\tPROMPT:\n", prompt)
    
    # Send a POST request to the Llama API with the prompt
    try:
        response = requests.post(API_URL, headers=HEADERS, json={
            "inputs": prompt,
            "parameters": {
                "top_k": 2,
                "top_p": 0.5,
                "temperature": 1,
                "max_new_tokens": 300,
                "return_full_text": False
            }
        })
        llama_response = response.json()
        
        # Extract the response from Llama
        formatted_response = format_response(llama_response)
        
        #print("\nRAW LLAMA RESPONSE:", llama_response)
        #print("\n\t\tFormatted Llama Response:\n", formatted_response)
        
        return formatted_response
    except Exception as e:
        print(f"Llama3 Request Failed: {e}")
        return []


def llama(user_query, datasheet_content):
    response = send_request(user_query, datasheet_content)
    
    return process(response)


if __name__ == "__main__":
    with open("data/LCM300.md", "r") as file:
            datasheet_content = file.read()
    
    user_query = "What is the efficiency of lcm300?"
    
    llama(user_query, datasheet_content)
