#%%
from collections import defaultdict
import re
import copy
import logging

#logging.basicConfig(level=logging.DEBUG)

def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> tuple[dict[int, list[str]], list[tuple[int]]]:
    # return assignment pairs
    assert content.count("\n\n") == 1
    
    configuration, steps = map(str.splitlines, content.split("\n\n"))

    # process configuration
    stacks = defaultdict(list)
    for line in configuration:
        for stack, crate in enumerate(line[1::4], start=1):
            if crate.isalpha():
                stacks[stack].insert(0, crate)

    # process steps
    steps = [tuple(map(int, step.split()[1::2])) for step in steps]

    logging.debug(f"{stacks=}")
    logging.debug(f"{steps=}")

    return stacks, steps


def rearrange(stacks: dict[int, list[str]], steps: list[tuple[int]], new_mover: bool = False) -> dict[int, list[str]]:
    rearranged_stacks = copy.deepcopy(stacks)
    
    for step in steps:
        logging.debug(f"{step=}")
        no_crate, from_stack, to_stack = step
        assert no_crate > 0 and from_stack > 0 and to_stack > 0
        assert from_stack in stacks and to_stack in rearranged_stacks
        
        moving_crates = rearranged_stacks[from_stack][-no_crate:]
        if not new_mover:
            moving_crates = moving_crates[::-1]
        logging.debug(f"{moving_crates=}")
        rearranged_stacks[from_stack] = rearranged_stacks[from_stack][:-no_crate]
        rearranged_stacks[to_stack].extend(moving_crates)
        logging.debug(f"{step=}, {rearranged_stacks=}")
    
    return rearranged_stacks


def task1(file: str) -> str:
    content = load_data(file)
    stacks, steps = parse_data(content)
    new_stack = rearrange(stacks, steps)
    
    return "".join(new_stack[k][-1] for k in sorted(new_stack.keys()))


### PART II
def task2(file: str):
    content = load_data(file)
    stacks, steps = parse_data(content)
    new_stack = rearrange(stacks, steps, new_mover=True)
    
    return "".join(new_stack[k][-1] for k in sorted(new_stack.keys()))


#%%
if __name__ == "__main__":
    top = task1("input.txt")
    print("Task1:", top)

    top = task2("input.txt")
    print("Task2:", top)
    # %%
