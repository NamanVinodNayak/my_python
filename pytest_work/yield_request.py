import pytest

@pytest.fixture
def temp_user(request):
    # -------- SETUP (runs BEFORE the test) --------
    print(f"\n🟢 SETUP: creating data for {request.node.name}")

    user = {
        "name": "Alice",
        "age": 25,
        "test_name": request.node.name
    }

    yield user   # ⬅️ test runs HERE

    # -------- TEARDOWN (runs AFTER the test) --------
    print(f"\n🔴 TEARDOWN: cleaning up after {request.node.name}")

def test_user_name(temp_user):
    assert temp_user["name"] == "Alice"

def test_user_age(temp_user):
    assert temp_user["age"] == 25
