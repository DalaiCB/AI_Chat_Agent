import requests
from langchain.prompts import ChatPromptTemplate

from process_llama_response import process

API_URL = "https://bo1zekebo4gy1v0e.us-east-1.aws.endpoints.huggingface.cloud"
HEADERS = {
	"Accept" : "application/json",
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

PROMPT_TEMPLATE = """
Based on the search results, answer the user query.
User query: {user_query}
Search results: {dataframe_results}

Note: Please add "~~~" at the end of your answer. You shouldn't use lists or bullet points in your response as the table will be provided to the user. Also, this will be sent to the user so refer to the user as 'you' and not 'user'.

Assistant:
"""

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

def generate_text_from_dataframe(df, user_query):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(user_query=user_query, dataframe_results=df)
    print("\n\n\t\tPROMPT:\n", prompt)
    
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
        
        final_response = process(formatted_response)

        return final_response
    except Exception as e:
        print(f"Llama3 Request Failed: {e}")
        return []
