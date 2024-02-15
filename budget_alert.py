import pandas as pd

def generate_script(excel_file, output_file):
    # Read data from Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Open a text file for writing
    with open(output_file, 'w') as f:
        # Loop through rows in the DataFrame and generate the script
        for index, row in df.iterrows():
            name = row['name']
            project_number = row['project_number']
            project_id = row['project_id']
            email = row['email']

            script = f"""
{name} = {{
    display_name                = "{name}-budget_alert"
    project_number              = "projects/{project_number}"
    project_id                  = "{project_id}"
    notification_channel_email  = "{email}"
}}
"""

            # Write the generated script to the file
            f.write(script)
            f.write('\n')  # Add a newline for better readability

# Replace 'your_excel_file.xlsx' with the path to your Excel file
# Replace 'output_script.txt' with the desired output text file path
generate_script('book4.xlsx', 'output_script.txt')
