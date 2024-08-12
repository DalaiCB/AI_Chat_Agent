import os
import re
from icecream import ic

def list_md_files(directory):
    
    return [f for f in os.listdir(directory) if f.endswith('.md')]

def normalize_string(s):
    
    return re.sub(r'[\s\-_/]', '', s.lower())

def search_product_files(product_name):
    if "/" in product_name:
        product_name = product_name.replace("/", "\\")

    md_files = list_md_files('data/test_md')
    normalized_product_name = normalize_string(product_name)
    
    matches = []
    for md_file in md_files:
        normalized_md_file = normalize_string(md_file.replace('.md', ''))
        if normalized_product_name == normalized_md_file:
            matches.append(md_file)
    
    print("Matching files:", matches)

    return matches

if __name__ == "__main__":
    search_product_files('IGA 320/23')
