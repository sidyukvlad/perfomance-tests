# import httpx
# import time
#
# create_user_payload = {
#   "email": f"{time.time()}@example.com",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"
# }
#
# create_user_response = httpx.post(
#     "http://localhost:8003/api/v1/users",
#     json = create_user_payload
# )
# create_user_response_data = create_user_response.json()

import httpx
import time

client = httpx.Client(
    base_url="http://localhost:8003"
)
payload = {
  "email": f"{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
response = client.post(
    "/api/v1/users",
    json = payload,
    timeout = 5
)

print(response.text)