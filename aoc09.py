import numpy as np

def aoc09(filepath:str) -> int:
    solution = 0
    with open(filepath) as f:
        input = f.readline().split()
        #  read line by line till end
        while len(input) > 0:
            # calc diff till all 0
            history = np.array(input, dtype=np.int32)
            diffs = np.array(history[0])
            while np.any(history != 0):
                history = np.diff(history)
                diffs = np.append(history[0], diffs)
            # calculate the prediction
            pred = 0
            for i in diffs[1:]:
                pred = i - pred
            solution += pred
            input = f.readline().split()
    
    return solution

if __name__ == '__main__':
    solution = aoc09("09/input.txt")
    print("The solution is:", solution)