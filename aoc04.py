import pandas as pd
import numpy as np
from io import StringIO

def aoc04(filepath:str) -> int:
    points = 0
    
    with open(filepath) as f:
        input = f.read()
        # prepare for csv parsing
        input = input.replace("Card ", "").replace(": ", "|")
        #  parse csv
    cards = pd.read_csv(StringIO(input), sep="|", index_col=0, header=None, names=["win", "draw"])
    # convert to data columns np.arrays
    cards= cards.map(lambda x: np.int16(x.split()))
    
    cards["compare"] = cards.apply(lambda x: np.in1d(x["draw"], x["win"]), axis=1)
    cards["right"] = cards["compare"].map(np.sum)
    cards["points"] = cards["right"].apply(lambda x: 2**(x-1) if x else 0)
    
    points = np.sum(cards["points"])


    return points

if __name__ == '__main__':
    solution = aoc04("04/input.txt")
    print("The solution is:", solution)