import os
import pandas as pd

def list_files_to_excel(folder_path, output_excel):
    # List to store file details
    file_data = []

    # Walk through the folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Append file details to the list
            file_data.append({
                "File Name": file,
                "File Path": file_path
            })
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(file_data)
    
    # Save to an Excel file
    df.to_excel(output_excel, index=False)

# Specify folder path and output file
folder_path = "huawei/jobs"  # Replace with your folder path
output_excel = "huawei/files_in_dataarts.xlsx"
list_files_to_excel(folder_path, output_excel)

print(f"File list has been saved to {output_excel}")
