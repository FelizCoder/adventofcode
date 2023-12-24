from io import StringIO
import pandas as pd
from math import lcm

def aoc08(filepath:str) -> int:
    step = 0
    with open(filepath) as f:
        input = f.read().replace(" ","").replace("=",",").replace("(", "").replace(")", "").splitlines()
        
    directions = input[0]
    map = dict()
    for line in input[2:]:
        line = line.split(",")
        map[line[0]] = (line[1:])
        
    step_list = []
    map = pd.DataFrame.from_dict(map, orient='index', columns=["L", "R"])

    start_pos = map.filter(regex='A$',axis=0).index
    
    for start in start_pos:
        pos = start
        step = 0
        while not pos.endswith("Z"):
            idx = step % len(directions)
            turn = directions[idx]
            pos = map.loc[pos][turn]
            step +=1
        step_list += [step]
        print (f"found Z for {start} at {pos} after {step} steps")
    
    # calc smallest common multiple
    step = lcm(*step_list)
    
    return step

if __name__ == '__main__':
    solution = aoc08("08/input.txt")
    print("The solution is:", solution)