import pytest
from solution import task1, task2

def test_task1():
    pairs = task1("test_input.txt")
    assert pairs == 2


#@pytest.mark.skip(reason="Not yet implemented")   
def test_task2():
    sum_ = task2("test_input.txt")
    assert sum_ == 4
