#%%
def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def str2range(section: str) -> set:
    start, end = map(int, section.split("-"))
    return set(range(start, end + 1))


def parse_data(content: str) -> list[list[str, str]]:
    # return assignment pairs
    return [map(str2range, l.split(",")) for l in content.splitlines()]


def fully_contains(pair: list[set, set]) -> bool:
    # see: https://realpython.com/python-sets/#available-operators-and-methods
    set_one, set_two = pair
    return set_one <= set_two or set_two <= set_one


def task1(file: str):
    content = load_data(file)
    pairs = map(fully_contains, parse_data(content))
    return sum(pairs)


### PART II
def overlap(pair: list[set, set]) -> bool:
    set_one, set_two = pair
    return bool(set_one & set_two)
    
def task2(file: str):
    content = load_data(file)
    pairs = map(overlap, parse_data(content))
    return sum(pairs)


if __name__ == "__main__":
    sum_ = task1("input.txt")
    print("Task1:", sum_)

    sum_ = task2("input.txt")
    print("Task2:", sum_)
    # %%
