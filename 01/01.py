import re

count = 0
p = re.compile(r'\d')

# include first and last letter in replacement for overlapping words
replacement = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8t"),
    ("nine","n9e")
]

with open("01/input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break

        # Replace spelled digits for filtering
        for old, new in replacement:
            line = line.replace(old,new)
        
        #  filter for digits
        digits = p.findall(line)
        count = count + int(digits[0] + digits[-1])
        
# solution
print("The calibration value is: ", count)