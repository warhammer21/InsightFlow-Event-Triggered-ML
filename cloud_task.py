import datetime
import json
from typing import Dict, Optional
from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2

def create_http_task(
    project: str,
    location: str,
    queue: str,
    url: str,
    json_payload: Dict,
    scheduled_seconds_from_now: Optional[int] = None,
    task_id: Optional[str] = None,
    deadline_in_seconds: Optional[int] = None,
) -> tasks_v2.Task:
    """Create an HTTP POST task with a JSON payload."""
    # Initialize Cloud Tasks client
    client = tasks_v2.CloudTasksClient()

    # Define the task with the HTTP request
    task = tasks_v2.Task(
        http_request=tasks_v2.HttpRequest(
            http_method=tasks_v2.HttpMethod.POST,
            url=url,
            headers={"Content-Type": "application/json"},
            body=json.dumps(json_payload).encode(),
        )
    )

    # Set task name if provided
    if task_id:
        task.name = client.task_path(project, location, queue, task_id)

    # Schedule for future time if specified
    if scheduled_seconds_from_now:
        timestamp = timestamp_pb2.Timestamp()
        timestamp.FromDatetime(datetime.datetime.utcnow() + datetime.timedelta(seconds=scheduled_seconds_from_now))
        task.schedule_time = timestamp

    # Set the deadline if specified
    if deadline_in_seconds:
        task.dispatch_deadline.seconds = deadline_in_seconds

    # Send the task creation request
    parent = client.queue_path(project, location, queue)
    response = client.create_task(parent=parent, task=task)

    print(f"Created task: {response.name}")
    return response


def delete_task(project: str, location: str, queue: str, task_id: str) -> None:
    """Delete a specified task."""
    # Initialize Cloud Tasks client
    client = tasks_v2.CloudTasksClient()

    # Construct the task name correctly
    task_name = f"projects/{project}/locations/{location}/queues/{queue}/tasks/{task_id}"

    # Delete the task
    client.delete_task(task_name)
    print(f"Deleted task: {task_name}")


# Define task parameters
project = "mindful-path-434005-m5"
location = "us-central1"
queue = "iflowmod"
url = "https://mindful-path-434005-m5.uc.r.appspot.com/predict"  # Replace with your App Engine endpoint
json_payload = {"data": [0.4, 0.6]}  # Modify as necessary
#task_id = "5772850237786470233"  # Specify your task ID for deletion

# Create the task
created_task = create_http_task(
    project=project,
    location=location,
    queue=queue,
    url=url,
    json_payload=json_payload,
)

# If you want to delete the task, uncomment the line below and ensure the task ID is correct
#delete_task(project, location, queue, task_id)
