import requests
import pytest

headers = {
    "Content-Type": "application/json",
    "Accept": "text/plain"
}

body = {
    "id": 2,
    "title": "strinnng",
    "dueDate": "2024-06-30T00:00:00Z"
}

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/5"

response = requests.put(url, json=body, headers=headers)

print(response.status_code)
print(response.json())

def test_status_code():
    assert response.status_code == 200