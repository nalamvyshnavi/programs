import new
def function_pytest_text(x):
    return x*10
def test_pytest_function():
    assert function_pytest_text(2)==20
    assert function_pytest_text(3)==40