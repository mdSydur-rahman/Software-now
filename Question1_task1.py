import pandas as pd
import os  # Import os module

# List of CSV file paths here
csv_files = [
    'C:\\Users\\surface\\Desktop\\HIT137 Software now\\Assignment 2\\CSV1.csv',
    'C:\\Users\\surface\\Desktop\\HIT137 Software now\\Assignment 2\\CSV2.csv',
    'C:\\Users\\surface\\Desktop\\HIT137 Software now\\Assignment 2\\CSV3.csv',
    'C:\\Users\\surface\\Desktop\\HIT137 Software now\\Assignment 2\\CSV4.csv'
]

# Output text file path
output_file = 'all_texts.txt'

# Define possible column names for text extraction
column_names = {
    'CSV1': 'SHORT-TEXT',
    'CSV2': 'TEXT',
    'CSV3': 'TEXT',
    'CSV4': 'TEXT'
}

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    for file in csv_files:
        df = pd.read_csv(file)
        
        # Clean column names by stripping extra spaces
        df.columns = df.columns.str.strip()
        
        # Determine which column to use based on the file name
        file_name = os.path.basename(file)
        key = file_name.split('.')[0]  # Extract file name without extension
        text_column = column_names.get(key, None)
        
        if text_column and text_column in df.columns:
            short_texts = df[text_column].dropna()
            for text in short_texts:
                outfile.write(text + '\n')  # Write text with newline
        else:
            print(f"'{text_column}' column not found in {file}")

print(f"Text data extracted and saved to {output_file}")

