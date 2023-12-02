import re

# define color regex
green_p = re.compile(r"(\d*) green")
red_p = re.compile(r'(\d*) red')
blue_p = re.compile(r'(\d*) blue')

with open("02/input.txt") as f:
    i = 0
    count = 0
    possible_i = []
    while True:
        i = i+1
        # 1 game per line
        game = f.readline()
        if not game:
            break
        
        # sets within a game are divided by ";"
        game = game.split(";")
        
        possible = True
        for set in game:
            # get count of each color
            green_m = green_p.search(set)
            red_m = red_p.search(set)
            blue_m = blue_p.search(set)
            
            if (green_m and int(green_m.group(1)) > 13):
                possible = False
                break
            if (red_m and int(red_m.group(1)) > 12):
                possible = False
                break
            if (blue_m and int(blue_m.group(1)) > 14):
                possible = False
                break  
        
        if possible:
            count = count + i
            
print(count)
            
            