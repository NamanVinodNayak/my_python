import pytest

@pytest.fixture
def number(request):
    print(f"Setting up number with value: {request.param}")
    return request.param * 10

@pytest.mark.parametrize("number", [1, 2, 3], indirect=True)
def test_something(number):
    assert number > 0
