import icecream as ic


# Function to extract product names from a given query text
def extract_product_names(query_text):
    # Convert the query text to lowercase for case-insensitive matching
    lower_query = query_text.lower()
    
    special_name = ["evergreen", "vento", "evergreen vento"]
    matched_names = []
    
    # Check if the query text contains any special product name
    for term in special_name:
        if term in lower_query:
            matched_names.append("FCM10K")
            break
    
    # Read product names from the text file
    with open("data/product_names.txt", "r") as file:
        product_names = [line.strip() for line in file]

    # Iterate over each product name
    for product_name in product_names:
        # Convert the product name to lowercase for case-insensitive matching
        lower_product_name = product_name.lower()

        # Remove spaces and hyphens from the product name and query text for comparison
        formatted_query = lower_query.replace(" ", "").replace("-", "")
        formatted_product_name = lower_product_name.replace(" ", "").replace("-", "")

        # Check if the formatted product name is contained within the formatted query text
        if formatted_product_name in formatted_query:
            matched_names.append(product_name)

    # If no matching product name is found, return None
    return matched_names if matched_names else None


if __name__ == "__main__":
    prompt = "What is the output current of ge 150 series?"

    print(extract_product_names(prompt))