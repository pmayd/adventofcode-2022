#%%
from string import ascii_lowercase, ascii_uppercase

PRIORITIES = dict(
    (l, i) for i, l in enumerate(ascii_lowercase + ascii_uppercase, start=1)
)


def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> list[str]:
    # return inventory
    return content.splitlines()


def find_wrong_item(inventory: str) -> str:
    inventory_mid = len(inventory) // 2
    left, right = inventory[:inventory_mid], inventory[inventory_mid:]
    wrong_item = set(left) & set(right)
    assert len(wrong_item) == 1
    return wrong_item.pop()


def task1(file: str):
    content = load_data(file)
    inventory = parse_data(content)
    wrong_items = map(find_wrong_item, inventory)
    return sum(PRIORITIES.get(item, 0) for item in wrong_items)


### PART II
def find_batch_item(group: list[str]) -> str:
    badge_item = set.intersection(*map(set, group))
    assert len(badge_item) == 1
    return badge_item.pop()


def task2(file: str):
    content = load_data(file)
    inventory = parse_data(content)
    groups = [iter(inventory)] * 3
    return sum(PRIORITIES.get(find_batch_item(group), 0) for group in zip(*groups))


#%%
sum_ = task1("input.txt")
print("Task1:", sum_)


# %%
sum_ = task2("input.txt")
print("Task2:", sum_)
# %%
