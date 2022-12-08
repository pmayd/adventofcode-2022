import pytest
from solution import task1, task2
  

def test_task1():
    forest, trees = task1("test_input.txt")
    assert len(trees) == 21


#@pytest.mark.skip("Not yet implemented")
def test_task2():
    max_score = task2("test_input.txt")
    assert max_score == 8
