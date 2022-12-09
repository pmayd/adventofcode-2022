#%%
import logging
import numpy as np

#logging.basicConfig(level=logging.DEBUG)

def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> list[tuple[str, int]]:
    moves = [line.split() for line in content.splitlines()]
    moves = map(lambda m: (m[0], int(m[1])), moves)
    return list(moves)


class Head:
    def __init__(self):
        self.x, self.y = 0, 0
        self.path = []
        
    def move(self, dir: str) -> None:
        if dir == "R":
            self.x += 1
        elif dir == "U":
            self.y += 1
        elif dir == "L":
            self.x -= 1
        elif dir == "D":
            self.y -= 1
        self._update_path()
    
    def _update_path(self) -> None:
        self.path.append((self.x, self.y))
            
 
class Tail:
    def __init__(self):
        self.x, self.y = 0, 0
        self.path = []
        
    def follow(self, head: Head) -> None:
        # only follow when head is at least two fields away
        delta_x = head.x - self.x
        delta_y = head.y - self.y
        if abs(delta_x) == 2 or abs(delta_y) == 2:
            self.x += min(delta_x, 1) if delta_x > 0 else max(delta_x, -1)
            self.y += min(delta_y, 1) if delta_y > 0 else max(delta_y, -1)
        # we can always append current path, later use set to get unique fields      
        self._update_path()
        
    def _update_path(self) -> None:
        self.path.append((self.x, self.y))
        
    def get_no_unique_positions(self):
        return len(set(self.path))

### PART I
def task1(file: str) -> tuple[Head, Tail]:
    content = load_data(file)
    moves = parse_data(content)
    head = Head()
    tail = Tail()
    for dir, steps in moves:
        logging.debug(f"{dir} {steps}")
        for _ in range(steps):
            head.move(dir)
            tail.follow(head)
            logging.debug(f"Head({head.x},{head.y}), Tail({tail.x},{tail.y})")
    
    return head, tail


### PART II
def task2(file: str):
    content = load_data(file)
    moves = parse_data(content)
    rope = {"head": Head(), "tail": [Tail() for _ in range(9)]}
    for dir, steps in moves:
        logging.debug(f"{dir} {steps}")
        for _ in range(steps):
            head = rope["head"]
            head.move(dir)
            for i, tail in enumerate(rope["tail"]):
                tail.follow(head)
                head = tail
                logging.debug(f"Head({head.x},{head.y}), Tail {i}({tail.x},{tail.y})")
    
    return rope


#%%
if __name__ == "__main__": 
    #head, tail = task1("input.txt")
    #print("Task 1:", tail.get_no_unique_positions())

    
    rope = task2("input.txt")
    tail = rope["tail"][-1]
    print("Task 2:", tail.get_no_unique_positions())

# %%
