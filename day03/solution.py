#%%
from string import ascii_lowercase, ascii_uppercase

PRIORITIES = dict((l, i) for i, l in enumerate(ascii_lowercase + ascii_uppercase, start=1))

def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> list:
    # return inventory
    return content.splitlines()


def task1(file: str):
    content = load_data(file)
    inventory = parse_data(content)
    compartments = [(l[:len(l)//2], l[len(l)//2:]) for l in inventory]
    return sum(PRIORITIES.get((set(l) & set(r)).pop(), 0) for (l, r) in compartments)


def task2(file: str):
    content = load_data(file)
    inventory = parse_data(content)
    badges = [(set(i1) & set(i2) & set(i3)).pop() for (i1, i2, i3) in zip(inventory[::3], inventory[1::3], inventory[2::3])]
    return sum(PRIORITIES.get(b, 0) for b in badges)


#%%
sum_ = task1("input.txt")
print("Task1:", sum_)


# %%
sum_ = task2("input.txt")
print("Task2:", sum_)
# %%
