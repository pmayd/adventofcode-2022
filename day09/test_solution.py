import pytest
from solution import task1, task2
  

def test_task1():
    head, tail = task1("test_input.txt")
    assert tail.get_no_unique_positions() == 13


#@pytest.mark.skip("Not yet implemented")
@pytest.mark.parametrize("file, expected", [("test_input.txt", 1), ("test_input2.txt", 36)])
def test_task2(file: str, expected: int):
    rope = task2(file)
    tail = rope["tail"][-1]
    assert tail.get_no_unique_positions() == expected
