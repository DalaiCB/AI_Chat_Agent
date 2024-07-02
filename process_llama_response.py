def process(raw_llama_response):
    if "~~~" in raw_llama_response:
        extracted_text = raw_llama_response.split("~~~")[0].strip()
    else:
        extracted_text = raw_llama_response
        
    return extracted_text

if __name__ == "__main__":
    text = """
According to the information, the Sekidenko 4100T weighs 1.31 kg (4 channel version). ~~~

Please let me know if you need any further assistance! ~~~

Please let me know if you need any further assistance! ~~~

Please let me know if you need any further assistance! ~~~
"""

    print(process(text))