
import pytest
from solution import load_data, parse_data, rearrange, task1, task2
from operator import itemgetter

@pytest.fixture
def test_data():
    return load_data("test_input.txt")


def test_parse_data(test_data):
    stacks, steps = parse_data(test_data)

    assert len(stacks) == 3
    assert stacks[1] == ["Z", "N"]
    assert stacks[2] == ["M", "C", "D"]
    assert stacks[3] == ["P"]

    assert len(steps) == 4
    assert steps[0] == (1, 2, 1)
    assert steps[1] == (3, 1, 3)
    assert steps[2] == (2, 2, 1)
    assert steps[3] == (1, 1, 2)


def test_rearrange(test_data):
    stacks, steps = parse_data(test_data)
    new_stack = rearrange(stacks, steps)

    assert len(new_stack) == 3
    assert new_stack[1] == ["C"]
    assert new_stack[2] == ["M"]
    assert new_stack[3] == ["P", "D", "N", "Z"]
    

def test_task1():
    top = task1("test_input.txt")
    assert top == "CMZ"


def test_task2():
    top = task2("test_input.txt")
    assert top == "MCD"
