import os
import pytest

@pytest.fixture(params=[1, 2, 3], ids=["one", "two", "three"])
def number(request):
    return request.param

def test_num_plus_two(number):
    assert number> 2
    
@pytest.mark.xfail()
def test_num_times_three(number):
    assert number * 3 > 5