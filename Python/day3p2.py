from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT.Y22(DAY3IN)') # read input from dataset
lines = list(input.split('\n')) # split input intro list delimited by new line
lines = list(map(str.strip, lines)) # remove white space

# split list into groups of three
# [thelist[pos:pos + size] for pos in range(0, len(thelist), size)]
groups = [lines[n:n+3] for n in range(0, len(lines), 3)]

items_dict = {}
sum = 0
for group in groups:
    for elf in group:
        for item in set(elf): # remove duplicates from each elf
            if item not in items_dict:
                items_dict[item] = 1
            else:
                items_dict[item] += 1

    in_common = max(items_dict, key=items_dict.get)
    if in_common.islower():
        sum += ord(in_common) - 96
    else:
        sum += ord(in_common) - 38

    items_dict.clear()

print(sum)

datasets.write('Z00620.ADVPY(OUTPUT)', content = str(sum), append = False)

with open(r'/z/z00620/advpython22/output', 'w') as output:
    output.write(str(sum))