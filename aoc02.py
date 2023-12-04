import re


def aoc02(filepath: str):
    # define color regex
    green_p = re.compile(r"(\d*) green")
    red_p = re.compile(r'(\d*) red')
    blue_p = re.compile(r'(\d*) blue')

    with open(filepath) as f:
        count = 0
        while True:
            # 1 game per line
            game = f.readline()
            if not game:
                break
            # sets within a game are divided by ";"
            game = game.split(";")
            
            possible = True
            
            green_n, red_n, blue_n = 0, 0, 0
            
            
            for set in game:
                # get count of each color
                green_m = green_p.search(set)
                red_m = red_p.search(set)
                blue_m = blue_p.search(set)
                
                if (green_m):
                    green_n = max(int(green_m.group(1)), green_n)
                if (red_m):
                    red_n = max(int(red_m.group(1)), red_n)
                if (blue_m):
                    blue_n = max(int(blue_m.group(1)), blue_n)
                
            power = green_n * blue_n * red_n
            count = count + power

        return count
            
if __name__ == '__main__':
    count = aoc02("02/test.txt")
    print("The solution is: ", count)