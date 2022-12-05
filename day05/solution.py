#%%
from collections import defaultdict
import re
import copy
import logging
from operator import itemgetter

#logging.basicConfig(level=logging.DEBUG)

def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> tuple[dict[int, list[str]], list[tuple[int]]]:
    # return assignment pairs
    assert content.count("\n\n") == 1
    
    configuration, steps = content.split("\n\n")

    # process configuration
    stacks = defaultdict(list)
    no_stacks = int(re.findall(r"\s\d+", configuration.splitlines()[-1])[-1])

    for line in configuration.splitlines():
        for stack in range(1, no_stacks + 1):
            crate, line = line[:3], line[4:]
            if "[" in crate:
                stacks[stack].insert(0, crate.strip("[]"))

    # process steps
    steps = [tuple(map(int, re.findall(r"\s\d+", step))) for step in steps.splitlines()]

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
