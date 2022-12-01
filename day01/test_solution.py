from solution import task1, task2

def test_task1():
    calories, max_ = task1("test_input.txt")
    assert len(calories) == 5
    assert max_ == 24000
    
    
def test_task2():
    top_three, sum_ = task2("test_input.txt")
    assert len(top_three) == 3
    assert sum_ == 45000