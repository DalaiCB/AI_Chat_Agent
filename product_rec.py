import pandas as pd
import traceback
from openai import OpenAI
from icecream import ic
import re
import os
from functools import reduce


# Function to call OpenAI API and process the user query
def process_user_query(user_query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    
    # Column names that can be searched
    valid_column_names = [
        "Series", "Type", "Manufacturer", "Efficiency", 
        "OutputCurrent", "OutputVoltage", "InputVoltage", 
        "ControlType", "OutputPower", "NumberOfOutputs", 
        "Warranty", "OperatingTemp", "Application",
        "Length", "Width", "Height"
    ]
    
    # System prompt. Query processing instructions for the AI assistant
    sys_prompt = """
    You are an assistant that extracts values and their associated column names from user queries. 
    Match the extracted values with one of these columns: {}.

    Your response should follow this format:
    column name: value

    Guidelines:
    - Only extract the column names that are present in the query.
    - Do not add any symbols like '-' or '*' before each name and value pair.
    - For Operating Temperatures, use the following guide and format:
        - Don't use GREATER or LESS for operating temperatures.
        - If the query indicates a minimum operating temp, your output should look like "OperatingTemp: MIN [value]"
        - If the query indicates a maximum operating temp, your output should look like "OperatingTemp: MAX [value]"
        - If operating temp is given as a range, your output should look like "OperatingTemp: RANGE [lower temp] -- [upper temp]"
    - For Input Voltages (DON'T return GREATER, LESS, RANGE, MAX, MIN), use only the following format:
        - InputVoltage: value
        - If a range is give (e.g. 80 to 220), use the format "InputVoltage: lowerValue -- higherValue"
        - Special Case: If you find exactly "264" as a value in the query, determine whether
            it is exactly or up to or more than 264. Only if you determine it is more than, then return 265 as the value
    - For sizes, if only 2 dimensions are given, return the 2 dimensions as Length and Width. Also, determine if the query is asking for the exact size or the size that fits in the given space ("LESS value" because product dimension needs to be less).
        - If height is given as 1U or 2U, convert it to inches (1U = 1.75, 2U = 3.5).
    - For ranges, use one of the following formats except for Input Voltages:
        - column name: RANGE value1 -- value2
        - column name: GREATER value
        - column name: LESS value
    - For boolean values (Demo and Sample), return 'True' or 'False'.
    - For product types, use one of the following for the value:
        - Front End PSUs DC-input
        - Front End PSUs AC-input
        - Enclosed PSU
        - Open Frame Low Power PSUs
        - Configurable/Modular PSUs
        - External Adapters
    - If query gives application, then determine the application and return that as value. Here are the applications: Medical, Industrial, IT Infrastructure, Space-Constrained, Lighting, Horticulture. 
    - If query gives manufacturer name (Artesyn or SLPower), return that as value. If these 2 names doesn't appear in the query, don't return Manufacturer (any other name you find is not a manufacturer name). 
    - Capitalize the first letter if the query includes 'analog' or 'digital'.
    - If the query mentions a series (e.g., "CINT0000", "LCM3000", "GB00", "CSU000ADC"), format it as 'Series: series name'
    - Do not include units of measurement in the answer (e.g. W or Watts, V or Volts/Voltage, A or Amps/Amperes, Inches).
    """.format(", ".join(valid_column_names))

    prompt = f"Query: {user_query}"

    # Call the OpenAI API to process the user query
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ], 
        max_tokens=50
    )
    
    try:
        # Extract column name and value from the response
        message_content = response.choices[0].message.content.strip()
        print(f"\tExtracted Column Names and Values:\n{message_content}\n")

        column_names = []
        values = []
        
        lines = message_content.split('\n')
        
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                column_name = parts[0].strip()
                column_name = column_name.replace(' ', '')
                column_name = column_name.replace('-', '')
                value = parts[1].strip()
                
                if value == 'True':
                    value = True
                elif value == 'False':
                    value = False

                column_names.append(column_name)
                values.append(value)

        return column_names, values
    except Exception as e:
        ic("Error - process_user_query:", e)
        message = "There was an error while processing the user query. Please try again."
        return message


# Function to remove duplicates while preserving the order
def remove_duplicates_preserve_order(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


# Function to search for products
def search_products(user_query, disable_print):
    # Process the user query to extract column names and values
    column_names, search_values = process_user_query(user_query)
    
    # Load product recommendation data
    df = pd.read_csv('data/3.csv')

    # Initialize lists to store conditions and column names to print
    conditions = []
    print_names = []

    # Search for products based on the extracted column names and values
    try:
        for col, val in zip(column_names, search_values):
            # Searching Application
            if col == "Application":
                ic()
                condition = (df[col].str.contains(val, flags=re.IGNORECASE, regex=True))
                conditions.append(condition)
                continue
            
            # Searching MinInputVoltage and MaxInputVoltage
            if "InputVoltage" in col:
                ic()
                print_names.append("MinInputVoltage")
                print_names.append("MaxInputVoltage")
                
                val = val.replace('LESS', '').replace('GREATER', '').replace('RANGE', '')

                if "--" in val: 
                    ic()
                    min_val, max_val = map(float, val.split('--'))
                    temp_val = max_val
                    ic(min_val, max_val)
                else: 
                    temp_val = float(val)
                    ic(temp_val)
                
                if temp_val >= 80.0 and temp_val <= 264.0:                   
                    ic()
                    condition = (df["MinInputVoltage"] >= 80.0) & (df["MaxInputVoltage"] <= 264.0)
                    conditions.append(condition)
                elif temp_val > 264.0 and temp_val <= 528.0:
                    ic()
                    condition = (df["MinInputVoltage"] > 150.0) & (df["MaxInputVoltage"] <= 528.0)
                    conditions.append(condition)
                elif temp_val < 0.0:
                    ic()
                    condition = (df["MinInputVoltage"] < 0.0) & (df["MaxInputVoltage"] < 0.0)
                    conditions.append(condition)
                else:
                    ic("Out of range InputVoltage value")
                    
                    if temp_val < 80:
                        condition = (df["MinInputVoltage"] == temp_val)
                        conditions.append(condition)
                    elif temp_val > 528:
                        condition = (df["MaxInputVoltage"] == temp_val)
                        conditions.append(condition)
                
                continue
            
            # Searching OperatingTemp
            if col == "OperatingTemp":
                ic()
                print_names.append("MinOperatingTemp")
                print_names.append("MaxOperatingTemp")

                if val.startswith('MIN') or 'MIN' in val:
                    ic()
                    condition = (df["MinOperatingTemp"] <= float(val.replace('MIN', '').strip()))
                    conditions.append(condition)
                elif val.startswith("MAX") or 'MAX' in val:
                    ic()
                    condition = (df["MaxOperatingTemp"] >= float(val.replace('MAX', '').strip()))
                    conditions.append(condition)
                elif val.startswith("RANGE") or '--' in val:
                    ic()
                    range_string = val.replace('RANGE', '').strip()
                    
                    min_value, max_value = map(float, range_string.split('--'))
                        
                    range_min = (df["MinOperatingTemp"] <= min_value)
                    range_max = (df["MaxOperatingTemp"] >= max_value)
                    
                    conditions.extend([range_min, range_max])
                continue
            
            # Searching Manufacturer and Series
            if col == "Series" or col == "Manufacturer":
                ic()
                condition = (df[col].str.contains(val, flags=re.IGNORECASE, regex=True))
                conditions.append(condition)
                continue
            
            # Searching Size
            if col == "Length" or col == "Width" or col == "Height":
                print("\nThis is COL:", col)
                ic()
                print_names.append("Length")
                print_names.append("Width")
                print_names.append("Height")
                
                if val.startswith('LESS') or 'LESS' in val:
                    ic()
                    max_value = float(val.replace('LESS', '').strip())
                    condition = (df[col] <= max_value)
                    conditions.append(condition)
                else:
                    ic()
                    condition = (df[col] == float(val))
                    conditions.append(condition)

                continue
            
            # Searching all other columns
            ic("General Case")
            print(f"\nSaving {col} to print_names list.")
            print_names.append(col)

            # Check if the value is a boolean. (Demo and Sample)
            if isinstance(val, bool):
                ic()
                condition = (df[col] == val)
                conditions.append(condition)
            elif val.startswith('RANGE') or '--' in val:
                ic()
                range_string = val.replace('RANGE', '').strip()
                
                min_value, max_value = map(float, range_string.split('--'))
                    
                range_min = (df[col] >= min_value)
                range_max = (df[col] <= max_value)
                
                conditions.extend([range_min, range_max])
            elif val.startswith('GREATER') or 'GREATER' in val:
                ic()
                min_value = float(val.replace('GREATER', '').strip())
                condition = (df[col] >= min_value)
                conditions.append(condition)
            elif val.startswith('LESS') or 'LESS' in val:
                ic()
                max_value = float(val.replace('LESS', '').strip())
                condition = (df[col] <= max_value)
                conditions.append(condition)
            else:
                ic()
                if val.isdigit():
                    condition = (df[col] == float(val))
                    conditions.append(condition)
                else:
                    ic()
                    condition = (df[col] == val)
                    conditions.append(condition)
        
        # Fill all NaN values with False
        combined_condition = reduce(lambda x, y: x & y, conditions)        
        combined_condition = combined_condition.fillna(False)

        # Display all rows and columns.
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        # Filter the DataFrame based on the combined condition
        filtered_df = df[combined_condition]

        # If the filtered DataFrame is empty, return a message
        if filtered_df.empty:
            ic("EMPTY DATAFRAME")

            return "NO PRODUCTS FOUND"

        # Columns to display in the output
        all_columns = ['Series', 'PartNumber', 'Manufacturer'] + print_names
        unique_columns = remove_duplicates_preserve_order(all_columns)

        if disable_print is False:
            print(filtered_df[unique_columns])

        # Remove the 'Application' column if it is present
        if "Application" in unique_columns:
            unique_columns.remove("Application")

        return filtered_df[unique_columns]
    except Exception as e:
        ic("Error - search_products:", e)
        traceback.print_exc()
        message = "There was an error while searching for products. Please try again."
        return message


if __name__ == "__main__":
    user_query = "recommend a product whose output power greater than 1000 W"
    ic("User Query:", user_query)
    try:
        search_products(user_query, disable_print=False)
    except Exception as e:
        ic("Error - Main:", e)
