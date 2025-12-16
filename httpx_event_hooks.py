from httpx import Client, Request, Response
from datetime import datetime

def log_request(request: Request):
    print(f"REQUEST: {request.method}")

def log_response(response: Response):
    print(f"RESPONSE: {response.status_code}")

client = Client(
    base_url="http://localhost:8003",
    event_hooks={"request": [log_request], "response": [log_response]}
)
response = client.get("/api/v1/users/ea39a37f-450d-418b-987b-957ce8ac4275")

# print(response.text)