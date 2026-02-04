import pytest

def sum_num():
    return 1 + 1

@pytest.mark.skip
def test_sum():
    assert sum_num() == 2
    
@pytest.mark.skipif(1==1,reason="skip needed")
def test_sum_plus_two():
    assert sum_num()+2 == 4

def test_sub_num():
    assert sum_num() -1 == 1