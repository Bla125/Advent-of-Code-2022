from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT.Y22(DAY1IN)')
line = list(input.split('\n'))
line = list(map(str.strip, line))

elf_dict = {}
elf_cals = 0

elf = 0

for i in (line):
    if i != '':
        elf_cals += int(i)

    elif i == '':
        elf_dict[int(elf_cals)] = elf
        elf += 1
        elf_cals = 0
elf_dict[int(elf_cals)] = elf


max_cal = max(elf_dict)

print(max_cal)
datasets.write('Z00620.ADVPY(OUTPUT)', content = str(max_cal), append = False)
