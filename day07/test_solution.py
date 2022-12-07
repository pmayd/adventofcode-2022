import pytest
from solution import task1, task2, get_dirs, load_data


def test_get_dirs():
    filesystem = load_data("test_input.txt")
    dirs = get_dirs(filesystem)
    assert len(dirs) == 4
    
    dir_e = [d for d in dirs if d.name == "e"][0]
    assert dir_e.size == 584
    
    dir_a = [d for d in dirs if d.name == "a"][0]
    assert dir_a.size == 94853
    
    dir_d = [d for d in dirs if d.name == "d"][0]
    assert dir_d.size == 24933642
    
    root = dirs[0]
    assert root.size == 48381165
    

def test_task1():
    total_size = task1("test_input.txt")
    assert total_size == 95437


#@pytest.mark.skip("Not yet implemented")
def test_task2():
    total_size = task2("test_input.txt")
    assert total_size == 24933642
