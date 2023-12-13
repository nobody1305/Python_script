import gitlab

# Replace with your GitLab URL and API token
gitlab_url = 'https://gitrepo.xlaxiata.id/'
api_token = 'ip2ygJ8X-fpXrgfHR1Lw'

# Create a GitLab API client
gl = gitlab.Gitlab(gitlab_url, private_token=api_token, api_version='4')

# Get all projects
projects = gl.projects.list(all=True)

# Print project information
for project in projects:
    print(f"Project ID: {project.id}, Name: {project.name}, URL: {project.web_url}")

# You can access other project details using the project object
# For example, project.description, project.owner, etc.
