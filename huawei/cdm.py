import pandas as pd
import json
import re

# Script 1 Functions
def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def extract_job_data(json_data):
    job_data = []
    number = 0
    for job in json_data['jobs']:
        number += 1
        job_name = job.get('name')
        from_link_name = job.get('from-link-name')
        to_link_name = job.get('to-link-name')

        to_job_config = next(
            (config for config in job.get('to-config-values', {}).get('configs', [])
             if config.get('name') == 'toJobConfig'), None)
        
        to_output_directory = None
        if to_job_config:
            for input_item in to_job_config.get('inputs', []):
                if input_item.get('name') == 'toJobConfig.outputDirectory':
                    to_output_directory = input_item.get('value')
                    break
        
        from_job_config = next(
            (config for config in job.get('from-config-values', {}).get('configs', [])
             if config.get('name') == 'fromJobConfig'), None)
        
        from_input_directory = None
        if from_job_config:
            for input_item in from_job_config.get('inputs', []):
                if input_item.get('name') == 'fromJobConfig.inputDirectory':
                    from_input_directory = input_item.get('value')
                    break
        
        group_job_config = next(
            (config for config in job.get('driver-config-values', {}).get('configs', [])
             if config.get('name') == 'groupJobConfig'), None)
        
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

# Script 2 Functions
def extract_data(json_obj):
    results = {}
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    for link in json_obj.get("links", []):
        link_name = link.get("name", "Unknown")
        configs = link.get("link-config-values", {}).get("configs", [])
        ips = set()
        username = None
        port = None
        
        for config in configs:
            for input_item in config.get("inputs", []):
                name = input_item.get("name", "")
                value = input_item.get("value", "")
                
                if isinstance(value, str):
                    ips.update(ip_pattern.findall(value))
                if name == "linkConfig.username":
                    username = value
                elif name == "linkConfig.port":
                    port = value
        
        if link_name not in results:
            results[link_name] = {"IP Addresses": set(), "Username": username, "Port": port}
        results[link_name]["IP Addresses"].update(ips)

    final_results = [
        {
            "Link Name": name,
            "IP Addresses": ", ".join(sorted(data["IP Addresses"])),
            "Username": data["Username"],
            "Port": data["Port"],
        }
        for name, data in results.items()
    ]
    return final_results

# Main Function
def main():
    # File paths
    json_file = 'huawei/cdm_cluster_2.json'
    excel_file = 'huawei/job_data_cluster_2.xlsx'
    
    # Read JSON
    data = read_json(json_file)
    
    # Script 1: Extract job data
    job_data = extract_job_data(data)
    df_jobs = pd.DataFrame(job_data, columns=["No", "Job Name", "Source Link", "Destination Link", "Input Directory", "Output Directory", "Group Name", "Time Filter"])
    
    # Script 2: Extract link data
    link_data = extract_data(data)
    df_links = pd.DataFrame(link_data)
    
    # Write to Excel with multiple sheets
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df_jobs.to_excel(writer, sheet_name='Jobs', index=False)
        df_links.to_excel(writer, sheet_name='Links', index=False)
    
    print(f"Data has been saved to {excel_file} with two sheets: 'Jobs' and 'Links'.")

# Run the script
if __name__ == '__main__':
    main()
