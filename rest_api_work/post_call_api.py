import requests
import pytest

base_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

head = {
    "Content-Type": "application/json"
}

data_payload = {
    "id": 1,
    "title": "string",
    "dueDate": "2024-06-30T00:00:00Z"
}

response = requests.post(base_url, headers=head, json=data_payload)

print(response.status_code)
print(response.json())

def test_status_code():
    assert response.status_code == 200
    