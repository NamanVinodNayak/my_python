import pytest

@pytest.fixture
def number():
    return 10

def test_num_plus_two(number):
    assert number + 2 == 12
    
def test_num_times_three(number):
    assert number * 3 == 30