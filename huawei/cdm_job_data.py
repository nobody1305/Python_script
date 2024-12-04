import pandas as pd
import json

# Read JSON file
def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def extract_job_names(json_data):
    # Extract the job names (from the 'jobs' list)
    job_names = [job['name'] for job in json_data['jobs']]
    return job_names

def extract_job_names_and_links(json_data):
    # Extract job names and to-link-names from the 'jobs' list
    job_data = []
    for job in json_data['jobs']:
        job_name = job.get('name')
        to_link_name = job.get('to-link-name')
        job_data.append([job_name, to_link_name])
    return job_data

# Extract job data (including toJobConfig.outputDirectory, fromJobConfig.inputDirectory, and groupJobConfig.groupName)
def extract_job_data(json_data):
    job_data = []
    number = 0
    for job in json_data['jobs']:
        number += 1
        job_name = job.get('name')
        from_link_name = job.get('from-link-name')
        to_link_name = job.get('to-link-name')
        
        # Extract toJobConfig.outputDirectory from to-config-values
        to_job_config = next(
            (config for config in job.get('to-config-values', {}).get('configs', [])
             if config.get('name') == 'toJobConfig'), None)
        
        # Find the outputDirectory value within the toJobConfig inputs
        to_output_directory = None
        if to_job_config:
            for input_item in to_job_config.get('inputs', []):
                if input_item.get('name') == 'toJobConfig.outputDirectory':
                    to_output_directory = input_item.get('value')
                    break
        
        # Extract fromJobConfig.inputDirectory from from-config-values
        from_job_config = next(
            (config for config in job.get('from-config-values', {}).get('configs', [])
             if config.get('name') == 'fromJobConfig'), None)
        
        # Find the inputDirectory value within the fromJobConfig inputs
        from_input_directory = None
        if from_job_config:
            for input_item in from_job_config.get('inputs', []):
                if input_item.get('name') == 'fromJobConfig.inputDirectory':
                    from_input_directory = input_item.get('value')
                    break
        
        # Extract groupJobConfig.groupName from driver-config-values
        group_job_config = next(
            (config for config in job.get('driver-config-values', {}).get('configs', [])
             if config.get('name') == 'groupJobConfig'), None)
        
        # Find the groupName value within the groupJobConfig inputs
        group_name = None
        if group_job_config:
            for input_item in group_job_config.get('inputs', []):
                if input_item.get('name') == 'groupJobConfig.groupName':
                    group_name = input_item.get('value')
                    break

        
        use_time_filter = next(
            (config for config in job.get('from-config-values', {}).get('configs', [])
             if config.get('name') == 'fromJobConfig'), None)
        
        time_filter = None
        if use_time_filter:
            for input_item in use_time_filter.get('inputs', []):
                if input_item.get('name') == 'fromJobConfig.useTimeFilter':
                    time_filter = input_item.get('value')
                    break
        
        job_data.append([number, job_name, from_link_name, to_link_name, to_output_directory, from_input_directory, group_name, time_filter])
    
    return job_data

# # Save DataFrame to Excel file
# def save_to_excel(job_names, excel_file):
#     job_names.to_excel(excel_file, index=False, engine='openpyxl')

# def save_to_excel(job_names, excel_file):
#     df = pd.DataFrame(job_names, columns=["Job Name"])
#     df.to_excel(excel_file, index=False, engine='openpyxl')

# def save_to_excel(job_data, excel_file):
#     df = pd.DataFrame(job_data, columns=["Job Name", "To-Link Name"])
#     df.to_excel(excel_file, index=False, engine='openpyxl')

def save_to_excel(job_data, excel_file):
    df = pd.DataFrame(job_data, columns=["No", "Job Name", "Source Link", "Destination Link", "Input Directory", "Output Directory", "Group Name", "Time Filter"])
    df.to_excel(excel_file, index=False, engine='openpyxl')

# Main function
def main():
    # Specify file paths
    json_file = 'huawei/cdm_20241204150433.json'  # Replace with your JSON file path
    excel_file = 'huawei/job_data.xlsx'  # Replace with your desired Excel file path
    
    # Step 1: Read data from the JSON file
    data = read_json(json_file)
    
    # Step 2: Convert JSON data to DataFrame
    job_data = extract_job_data(data)
    
    # Step 3: Save DataFrame to Excel
    save_to_excel(job_data, excel_file)
    
    print(f"Data from {json_file} has been added to {excel_file}.")

# Run the script
if __name__ == '__main__':
    main()
