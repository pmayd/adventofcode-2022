#%%
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional
from operator import attrgetter

#logging.basicConfig(level=logging.DEBUG)

@dataclass
class Dir:
    parent: Optional[Dir] = field(init=False)
    size: int = field(init=False)
    name: str

    def __post_init__(self):
        self.size = 0
        self.parent = None


def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def get_dirs(filesystem: str) -> list[Dir]:
    root = Dir("/")
    parent = root
    current_dir = root
    dirs = [root]
    for line in filesystem.splitlines():
        logging.debug(f"{line}")
        match line.split():
            case ["$", "cd", name] if name not in ["/", ".."]:                    
                parent = current_dir
                current_dir = Dir(name)
                current_dir.parent = parent
                dirs.append(current_dir)
                logging.debug(f"Entering dir {current_dir}.")
            case ["$", "cd", ".."]:
                current_dir = current_dir.parent
                if current_dir.parent is not None:
                    parent = current_dir.parent.parent
            case [size, file] if size not in ["dir", "$"]:
                update_dirs(current_dir, int(size))
    logging.debug(f"All dirs: {dirs}")
    return dirs


def update_dirs(dir: Dir, size: int):
    dir.size += size
    logging.debug(f"Update dir {dir.name} with size {size}. New size: {dir.size}.")
    if dir.parent is not None:
        update_dirs(dir.parent, size)


def task1(file: str) -> str:
    filesystem = load_data(file)
    dirs = get_dirs(filesystem)
    return sum(dir.size for dir in dirs if dir.size < 100000)


### PART II
total_space = 70000000
necessary_free_space = 30000000

def task2(file: str):
    filesystem = load_data(file)
    dirs = get_dirs(filesystem)
    logging.debug(f"Task 2:  {dirs}")
    
    root = dirs[0]
    unused_space = total_space - root.size
    required_space = necessary_free_space - unused_space
    
    for dir_ in sorted(dirs[1:], key=attrgetter("size")):
        if dir_.size >= required_space:
            return dir_.size



#%%
if __name__ == "__main__":
    total_size = task1("input.txt")
    print("Task1:", total_size)
    
    total_size = task2("input.txt")
    print("Task2:", total_size)

# %%
