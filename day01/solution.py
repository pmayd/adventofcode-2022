#%% 
def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> list:
    lines = content.splitlines()
    calories = []
    current_elve = 0
    while lines:
        line = lines.pop()
        if line:
            current_elve += int(line)
        else:
            calories.append(current_elve)
            current_elve = 0

    calories.append(current_elve)
    return calories
  

def task1(file: str):
    content = load_data(file)
    calories = parse_data(content)
    return calories, max(calories)


def task2(file: str):
    content = load_data(file)
    calories = parse_data(content)
    top_three = sorted(calories)[-3:]
    return top_three, sum(top_three)


#%%
cal, max_ = task1("input.txt")
print("Task1:", max_)


# %%
top_three, sum_ = task2("input.txt")
print("Task2:", sum_)