import pandas as pd
import numpy as np
from io import StringIO

def aoc04(filepath:str) -> int:
    with open(filepath) as f:
        input = f.read()
        # prepare for csv parsing
        input = input.replace("Card ", "").replace(": ", "|")
        #  parse csv
    cards = pd.read_csv(StringIO(input), sep="|", index_col=0, header=None, names=["win", "draw"])
    # convert to data columns np.arrays
    cards = pd.DataFrame(cards.map(lambda x: np.int16(x.split())))
    
    cards["instances"] = 1
    cards["compare"] = cards.apply(lambda x: np.in1d(x["draw"], x["win"]), axis=1)
    cards["right"] = cards["compare"].map(np.sum)

    for i, card in cards.iterrows():
        cards.loc[i+1:i+card["right"], "instances"] += 1 * cards.loc[i,"instances"]

    cards = np.sum(cards["instances"])
    return cards

if __name__ == '__main__':
    solution = aoc04("04/input.txt")
    print("The solution is:", solution)