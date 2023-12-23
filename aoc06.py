import math

def aoc06(filepath:str) -> int:
    solution = 1
    with open(filepath) as f:
        input = f.readlines()
    
    times = input[0].split(":")[-1].split()
    dists = input[1].split(":")[-1].split()

    for (time, dist) in zip(times, dists):
        min, max = calc_timespan(float(time), float(dist))    
        span = max - min + 1
        if span:
            solution *= span
    return solution

def calc_timespan(t: float, s: float) -> tuple[float]:
    max = t/2 + (t**2/4-s)**0.5
    min = t/2 - (t**2/4-s)**0.5
    
    return (math.ceil(min+1e-6), math.floor(max-1e-6))

if __name__ == '__main__':
    solution = aoc06("06/input.txt")
    print("The solution is:", solution)