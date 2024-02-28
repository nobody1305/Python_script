from google.cloud import container_v1
from googleapiclient import discovery
import os
from google.cloud import monitoring_v3
import time
import xlsxwriter

# add to xlxs
project_id = 'anthos-alpha-5929'
zone = 'asia-southeast2'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'application_default_credentials.json'


def cluster(project_id, zone):
    cluster_client = container_v1.ClusterManagerClient()
    rows =[]
    # get all cluster on the project
    parent = f'projects/{project_id}/locations/{zone}'
    clusters = cluster_client.list_clusters(parent=parent)
    for cluster in clusters.clusters:
        rows.append(["", "Kubernetes Cluster: ", cluster.name, f"Version: {cluster.current_master_version}"])
        rows += instance(project_id, cluster.name)
    if not rows:
        rows.append(["", "Kubernetes Cluster: ", "No Cluster Found"])
    return rows

def instance(project_id, cluster=None):
    monitoring_client = monitoring_v3.MetricServiceClient()
    rows = []
    rows += [["No", "Instance Name", "Machine Type","Public IP Address","Private IP Address" ,  "CPU Utilization"]]
    compute = discovery.build('compute', 'v1')
    project_name = f"projects/{project_id}"
    zones = ['asia-southeast2-a', 'asia-southeast2-b', 'asia-southeast2-c']
    # get compute engine instance
    i=1
    for zone in zones:
        try:
            request = compute.instances().list(project=project_id, zone=zone)
            response = request.execute()
            if not response.get("items"):
                continue

        except:
            continue

        for instance in response['items']:

            label = instance.get('labels')
            if not label:
                label = {}
                
            if label.get('goog-k8s-cluster-name') == cluster:
                # get all the internal ip address
                public_ips = []
                private_ips = []
                for network_interface in instance['networkInterfaces']:
                    private_ips.append(network_interface['networkIP'])
                    try:
                        public_ip = network_interface.get('accessConfigs')[0].get('natIP')
                    except:
                        public_ip = None
                    if public_ip:
                        public_ips.append(public_ip)
                public_ips = ', '.join(public_ips)
                private_ips = ', '.join(private_ips)


    
                rows.append([i, instance['name'], instance['machineType'].split('/')[-1], public_ips, private_ips])
                i += 1
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 240), "nanos": nanos},
        }
    )

    results = monitoring_client.list_time_series(
        request={
            "name": project_name,
            "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )
    for i in range(len(rows)):
        for result in results:
            if rows[i][1] == result.metric.labels['instance_name']:
                rows[i].append(f'{round(result.points[0].value.double_value * 100,2)} %')
    rows.append([])
    return rows


def db(project_id):
    rows = []
    rows += [["No", "Instance Name", "DB Version", "Storage Used", "CPU Utilization"]]
    service = discovery.build('sqladmin', 'v1beta4')
    project_name = f"projects/{project_id}"
    monitoring_client = monitoring_v3.MetricServiceClient()
    dbdata = service.instances().list(project=project_id).execute()
    if not dbdata.get("items"):
        return rows
    i=1
    for instance in dbdata['items']:
        rows.append([i, instance['name'], instance['databaseVersion']])
        i+=1

    
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 240), "nanos": nanos},
        }
    )

    results = monitoring_client.list_time_series(
        request={
            "name": project_name,
            "filter": 'metric.type = "cloudsql.googleapis.com/database/disk/bytes_used"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )

    results_cpu = monitoring_client.list_time_series(
    request={
        "name": project_name,
        "filter": 'metric.type = "cloudsql.googleapis.com/database/cpu/utilization"',
        "interval": interval,
        "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
    }
)

    for result in results:
        for i in range(len(rows)):
            if rows[i][1] == result.resource.labels['database_id'].split(':')[1]:
                rows[i].append(f'{round(result.points[0].value.int64_value / 1024 / 1024 / 1024,2)} GB')

    for result in results_cpu:
        for i in range(len(rows)):
            if rows[i][1] == result.resource.labels['database_id'].split(':')[1]:
                rows[i].append(f'{round(result.points[0].value.double_value * 100,2)} %')
        
    return rows

def load_balancer(project_id):
    rows = []
    rows += [["No", "Load Balancer Name","Load Balancer Type"]]
    compute = discovery.build('compute', 'v1')
    project_name = f"projects/{project_id}"
    request = compute.forwardingRules().list(project=project_id, region='asia-southeast2')
    response = request.execute()
    i=1
    for instance in response['items']:
        # get load balancer protocol
        load_balancer_protocol = instance['IPProtocol']  
        protocols = ['TCP', 'UDP', 'ESP', 'GRE', 'ICMP', 'ICMPv6'] 
        if load_balancer_protocol in protocols:
            load_balancer_protocol = 'Network'
        elif load_balancer_protocol == 'HTTP' or load_balancer_protocol == 'HTTPS':
            load_balancer_protocol = 'Application'

        rows.append([i, instance['name'] , load_balancer_protocol])
        i+=1
    return rows 

def write_to_excel(title, **contents):
    workbook = xlsxwriter.Workbook(f'GCP_{title}_inventory.xlsx')
    for sub in contents:
        worksheet = workbook.add_worksheet(sub)
        content = contents[sub]
        for row in range(len(content)):
            for col in range(len(content[row])):
                worksheet.write(row, col, content[row][col])
    workbook.close()

if __name__ == '__main__':
    row_cluster = cluster(project_id, zone)
    row_instance = instance(project_id)
    row_db = db(project_id)
    row = load_balancer(project_id)
    write_to_excel(project_id, cluster=row_cluster, vm=row_instance, db=row_db, load_balancer=row)
