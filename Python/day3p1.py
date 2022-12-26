from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT.Y22(DAY3IN)') # read input from dataset
line = list(input.split('\n')) # split input into list delimited by new line
line = list(map(str.strip, line)) # strip white space


def find_dupicates(lines):
    left_side = set()
    right_side = set()
    sum = 0

    for line in lines:                                  # loop through input line by line
        for letter in range(len(line)//2):              # loop through first half of line
            if line[letter] not in left_side:           # get rid of duplicate letters in first half
                left_side.add(line[letter])             # add unique letters to set

        for letter in range(len(line)//2, len(line)):   # loop through second half of line
            if line[letter] not in right_side:          # get rid of duplicate letters in second half
                right_side.add(line[letter])            # add unique letters to set

        for letter in left_side:                        # loop through letters in left side of line
            if letter in right_side:                    # if any letters in the left side are also in the right side
                if letter.islower():                    # check if letter is lower case
                    sum += ord(letter) - 96             # get position of letter in alphabet through ascii arithmetic
                else:                                   # letter is uppercase
                    sum += ord(letter) - 38             # get position of letter in alphabet through ascii arithmetic

        # remove all elements of sets
        left_side.clear()
        right_side.clear()
         
    return sum

answer = find_dupicates(line)

print(answer)

datasets.write('Z00620.ADVPY(OUTPUT)', content = str(answer), append = False)

with open(r'/z/z00620/advpython22/output', 'w') as output_file:
    output_file.write(str(answer))
