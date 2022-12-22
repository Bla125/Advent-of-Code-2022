from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT.Y22(DAY2IN)') # read input from dataset
line = list(input.split('\n')) # separate input into list delimited by new line
line = list(map(str.strip, line)) # strip white space

# elf key
# a = rock
# b = paper 
# c = scissors

# my key
# x = rock 
# y = paper 
# z = scissors

# strategy guide
# A Y
# B X
# C Z

# x = 1
# y = 2
# z = 3

# lost = 0
# draw = 3
# win = 6


score = 0



# check first character of string [0], then check last character of string [-1]
for pair in line:
    if pair[0] == 'A': 
        if pair[-1] == 'X': score += 4 # draw
        elif pair[-1] == 'Y': score += 8 # win
        elif pair[-1] == 'Z': score += 3 # lose
    elif pair[0] == 'B': 
        if pair[-1] == 'X': score += 1 # lose
        elif pair[-1] == 'Y': score += 5 # draw
        elif pair[-1] == 'Z': score += 9 # win
    elif pair[0] == 'C': 
        if pair[-1] == 'X': score += 7 # win
        elif pair[-1] == 'Y': score += 2 # lose
        elif pair[-1] == 'Z': score += 6 # draw


datasets.write('Z00620.ADVPY(OUTPUT)', content = str(score), append = False)
