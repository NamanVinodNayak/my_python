import pytest

@pytest.fixture(scope="module",autouse=True)
def db_connection():
    print("\nSetting up database connection")
    yield
    print("\nTearing down database connection")
    
def test_query_1():
    print("Running test_query_1")
    assert True
    
def test_query_2():
    print("Running test_query_2")
    assert True
    
def test_query_3():
    print("Running test_query_3")
    assert True
    
def test_query_4():
    print("Running test_query_4")
    assert True

