import pandas as pd
from google.cloud import storage, tasks_v2
import json

def handle_storage_event(event, context):
    bucket_name = event['bucket']
    file_name = event['name']

    # Initialize the Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Download the file content as a string and parse it with pandas
    csv_data = blob.download_as_text()
    df = pd.read_csv(pd.compat.StringIO(csv_data), header=None)

    # Extract the 'data' column (assuming it’s the first column) as a JSON object
    data_values = json.loads(df.iloc[0, 0])  # Assumes data format is {"data": [...]}

    # Define the task
    client = tasks_v2.CloudTasksClient()
    task = {
        'http_request': {
            'http_method': tasks_v2.HttpMethod.POST,
            'url': 'https://mindful-path-434005-m5.uc.r.appspot.com/predict',  # Replace with your App Engine URL
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(data_values).encode()
        }
    }

    # Create the task
    queue_path = client.queue_path('mindful-path-434005-m5', 'us-central1', 'iflowmod')
    response = client.create_task(request={"parent": queue_path, "task": task})

    print(f"Created task {response.name}")
