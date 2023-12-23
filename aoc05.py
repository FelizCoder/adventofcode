import pandas as pd
import numpy as np
import re

def aoc05(filepath:str) -> int:
    seed = None
    with open(filepath) as f:
        input = f.read().split(":")
        
    # seeds of interest are in the Line after the first ":"
    # last elemts are declaration of next map
    
    seeds_ranges = np.int64(input[1].split()[:-2])
    seeds = []
    for i in range(0,len(seeds_ranges),2):
        seeds += list(range(seeds_ranges[i],seeds_ranges[i] + seeds_ranges[i+1]))
    
    # All seeds from lowest to highest
    
    almanach = pd.DataFrame(seeds, columns=["seeds"])
    
    dependencies = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    
    for i,dep in enumerate(dependencies):
        # each range is defined in a line after the ":"
        ranges = input[2+i].splitlines()
        # whitespace inbetween entries of a range
        ranges = np.int64([r.split() for r in ranges if re.sub(r'[^\d\s]','', r).strip()])
        # Perform Mapping
        ranges
        almanach[dep] = almanach.iloc[:,-1].apply(lambda x: almanach_mapping(x,ranges))
    
    # retun Seed with minimal location
    return almanach.location.min()
        

def almanach_mapping(source: np.int_, mapping: np.int_) -> int:
    """Maps from the Source column entry to Destination

    Args:
        source (np.int_): Singe entry from source Column
        mapping (np.int_): Coresponding Mappings

    Returns:
        int: _description_
    """    # split mapping into variables
    map_dest = mapping[:,0]
    map_source = mapping[:,1]
    map_length = mapping[:,2]

    # Check where source is within some range
    idx = np.argwhere(np.logical_and(map_source <= source, source < map_source + map_length))
    
    if idx.size > 0:
        output = map_dest[idx] + source - map_source[idx]
        return output.flatten()
    return source
if __name__ == '__main__':
    solution = aoc05("05/input.txt")
    print("The solution is:", solution)