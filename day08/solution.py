#%%
import logging
import numpy as np

#logging.basicConfig(level=logging.DEBUG)

def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def parse_data(content: str) -> np.array:
    forest = np.array([list(map(int, list(line))) for line in content.splitlines()])
    return forest


def count_visible_trees(forest: np.array) -> list[tuple[int, int]]:
    height, width = forest.shape
    visible_trees = []
    # traverse from top and bottom
    for i in range(height):
        for j in range(width):
            current_tree = forest[i,j]
            if i == 0 or j == 0:
                visible_trees.append((i,j))
                continue
            
            tree_lines = [
                forest[:i,j], # above
                forest[i,(j+1):], # right
                forest[(i+1):,j], # below
                forest[i,:j] # left
            ]
            # check each direction for only smaller trees until the edge
            for tree_line in tree_lines:
                if np.all(tree_line < current_tree):
                    visible_trees.append((i,j))
                    break
                
    return visible_trees


def calc_max_scenic_score(forest: np.array) -> int:
    height, width = forest.shape
    scores = []
    # traverse from top and bottom
    for i in range(1, height-1):
        for j in range(1, width-1):            
            current_tree = forest[i,j]
            score = 1
            
            tree_lines = [
                forest[:i,j][::-1], # above
                forest[i,(j+1):], # right
                forest[(i+1):,j], # below
                forest[i,:j][::-1] # left
            ]
            # check each direction for only smaller trees until the edge
            for tree_line in tree_lines:
                if np.all(tree_line < current_tree):
                    score *= len(tree_line)
                else:
                    for distance, tree in enumerate(tree_line):
                        if tree >= current_tree:
                            score *= distance + 1
                            break
            scores.append(score)
            
                
    return max(scores)


def visualize_forest(forest: np.array, visible_trees: list[tuple[int, int]]):
    height, width = forest.shape
    for i in range(height):
        for j in range(width):
            #print(f"({i},{j}) visible: {(i,j) in visible_trees}")
            if (i,j) in visible_trees:
                print("o", end="")
            else:
                print("x", end="")
        print()
            

def task1(file: str) -> str:
    content = load_data(file)
    forest = parse_data(content)
    visible_trees = count_visible_trees(forest)
    
    return forest, visible_trees


### PART II
def task2(file: str):
    content = load_data(file)
    forest = parse_data(content)
    max_score = calc_max_scenic_score(forest)
    
    return max_score


#%%
if __name__ == "__main__": 
    #forest, visible_trees = task1("input.txt")
    #visualize_forest(forest, visible_trees)
    #print("Task1:", len(visible_trees))
    
    max_score = task2("input.txt")
    print("Task2:", max_score)

# %%
