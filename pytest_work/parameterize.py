import pytest

def add_num(*args):
    return sum(args)

@pytest.mark.parametrize("a,b,c", [
    (1, 2, 3),
    (3, 4, 7),
    (5, 9, 14),
])
def test_add_two(a, b, c):
    assert add_num(a, b) == c