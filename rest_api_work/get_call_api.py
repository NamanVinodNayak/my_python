import requests
import pytest

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/1"

response = requests.get(url)

print(response.status_code)
print(response.json())

def test_status_code():
    assert response.status_code == 200
