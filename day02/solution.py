#%%
ENCRYPTED_MOVE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

MOVE_SCORE = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

STRATEGY_SCORE = {
    "rock": {
        "rock": 3,
        "paper": 6,
        "scissors": 0
    },
    "paper": {
        "rock": 0,
        "paper": 3,
        "scissors": 6
    },
    "scissors": {
        "rock": 6,
        "paper": 0,
        "scissors": 3
    }
}

ENCRYPTED_MOVE_PART_TWO = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loose",
    "Y": "draw",
    "Z": "win"
}

STRATEGY_MOVE = {
    "rock": {
        "win": "paper",
        "draw": "rock",
        "loose": "scissors"
    },
    "paper": {
        "win": "scissors",
        "draw": "paper",
        "loose": "rock"
    },
    "scissors": {
        "win": "rock",
        "draw": "scissors",
        "loose": "paper"
    }
}


def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str, part: int) -> list:
    total_score = sum(score_strategy(*line.split(), part=part) for line in content.splitlines())
    return total_score


def score_strategy(opponent: str, response: str, part: int) -> int:
    opponent = ENCRYPTED_MOVE[opponent]
    if part == 1:
        response = ENCRYPTED_MOVE[response]
    else:
        response = ENCRYPTED_MOVE_PART_TWO[response]
        response = STRATEGY_MOVE[opponent][response]
    return MOVE_SCORE[response] + STRATEGY_SCORE[opponent][response]


def task1(file: str):
    content = load_data(file)
    total_score = parse_data(content, part=1)
    return total_score


def task2(file: str):
    content = load_data(file)
    total_score = parse_data(content, part=2)
    return total_score


#%%
#total_score = task1("input.txt")
#print("Task1:", total_score)

# %%
total_score = task2("input.txt")
print("Task2:", total_score)
# %%
