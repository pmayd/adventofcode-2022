import pytest
from solution import task1, task2

def test_task1():
    total_score = task1("test_input.txt")
    assert total_score == 15


#@pytest.mark.skip(reason="Not yet implemented")   
def test_task2():
    total_score = task2("test_input.txt")
    assert total_score == 12
