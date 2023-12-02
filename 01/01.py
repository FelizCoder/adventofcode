import re

count = 0
p = re.compile(r'\d')

with open("01/input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        digits = p.findall(line)
        count = count + int(digits[0] + digits[-1])
        
print("The calibration value is: ", count)