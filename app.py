from streamlit.runtime.scriptrunner import get_script_run_ctx
from icecream import ic
import streamlit as st
import pandas as pd

from main import main
from text_from_dataframe import generate_text_from_dataframe


# Function to load URL from a file
def load_url(file_path):
    url_mappings = {}
    with open(file_path, 'r') as file:
        for line in file:
            series_name, page_url, datasheet_url = line.strip().split('~~')
            url_mappings[series_name] = {"page_url": page_url, "datasheet_url": datasheet_url}
    return url_mappings


# Function to add URLs to the DataFrame and convert Series names to hyperlinks
def add_urls_and_create_hyperlinks(df, url_mappings):
    df['Page URL'] = df['Series'].map(lambda x: url_mappings.get(x, {}).get('page_url', 'URL not found'))
    df['Datasheet URL'] = df['Series'].map(lambda x: url_mappings.get(x, {}).get('datasheet_url', 'URL not found'))
    
    df['Series'] = df.apply(
        lambda row: f'<a href="{row["Page URL"]}">{row["Series"]}</a>' if row["Page URL"] != 'URL not found' else row["Series"],
        axis=1
    )
    
    df['Datasheet'] = df.apply(
        lambda row: f'<a href="{row["Datasheet URL"]}">Datasheet</a>' if row["Datasheet URL"] != 'URL not found' else 'Datasheet not found',
        axis=1
    )
    
    return df


# Function to convert DataFrame to HTML table
def dataframe_to_html(df):
    return df.to_html(escape=False, index=False)


def format_message(message):
    ic(type(message))
    ic(message)
    # Replace newline characters with HTML line breaks
    message = message.replace('\n', '<br>')
    message = message.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')

    return message
    

def clear_sessions_file():
    with open('sessions.txt', 'w') as f:
        f.truncate(0)


def run_app():
    # Title
    st.title("AI Agent - Llama 3 8B")

    # Get sessions ID
    ctx = st.runtime.scriptrunner.get_script_run_ctx()
    session_id = ctx.session_id if ctx else "No session"

    # Chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Clear old chat history
    if "file_cleared" not in st.session_state:
        clear_sessions_file()
        st.session_state.file_cleared = True

    # Load URL
    urls = load_url('data/url.txt')

    prompt = st.chat_input("Message AE Chatbot")

    if prompt:
        response_text = main(prompt, session_id)

        # If response is a DataFrame, add URLs and create hyperlinks
        if isinstance(response_text, pd.DataFrame):
            summary = generate_text_from_dataframe(response_text, prompt)
            summary_html = format_message(summary)
            
            response_text = add_urls_and_create_hyperlinks(response_text, urls)
            response_text_html = dataframe_to_html(response_text.drop(columns=['Page URL', 'Datasheet URL']))
            
            combined_message = f"{summary_html}\n\n{response_text_html}"

            st.session_state.history.append((prompt, combined_message))
        else:
            st.session_state.history.append((prompt, format_message(response_text)))

    # Display the chat history
    for message, response in st.session_state.history:
        st.chat_message("user").markdown(format_message(message), unsafe_allow_html=True)
        
        if isinstance(response, str):  # Check if response is a string
            st.chat_message("bot").markdown(response, unsafe_allow_html=True)
        else:  # Assuming response is HTML if not a string (DataFrame case)
            st.markdown(response, unsafe_allow_html=True)


if __name__ == "__main__":
    run_app()
