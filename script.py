import os

# Define the text file containing folder names
input_file = "foldernames.txt"

try:
    # Open and read the file
    with open(input_file, 'r') as file:
        folder_names = file.readlines()
    
    # Iterate through each line in the file
    for folder_name in folder_names:
        # Strip any leading/trailing whitespace or newline characters
        folder_name = folder_name.strip()
        
        # Skip empty lines
        if not folder_name:
            continue
        
        # Create the folder if it doesn't already exist
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
