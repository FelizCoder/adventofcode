import re

def aoc03(filepath:str) -> int:
    parts = 0
    
    with open(filepath) as f:
        input = f.readlines()
    
    d_pat = re.compile(r'\d+')
    s_pat = re.compile(r'\*')
    
    for i,line in enumerate(input):
        # Check for digits in the line
        for star in s_pat.finditer(line):
            left, right = star.span()
            # define spans, limit out of bound indexes
            left = max(0,left-1)
            right = right + 1
            up = max(0,i-1)
            down = i+2
            
            # Get everything surrounding the digit
            area = [line[left:right] for line in input[up:down]]
            digits = [d_pat.findall(area_line) for area_line in area]
            
            if len(digits) > 1:
                parts = parts + int(star.group(0))
    
    return parts

if __name__ == '__main__':
    solution = aoc03("03/input.txt")
    print("The solution is:", solution)