from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT.Y22(DAY4IN)') # read input form dataset
lines = list(input.split('\n')) # split input into list delimited by new line
lines = list(map(str.strip, lines)) # remove white space
line = [i.split(',') for i in lines] 
nums = [[i.split('-') for i in j] for j in line]

total = 0

for i in range(len(nums)):
    if (int(nums[i][0][0]) <= int(nums[i][1][0])) and (int(nums[i][0][1]) >= int(nums[i][1][1])):
        total += 1
    elif (int(nums[i][1][0] )<= int(nums[i][0][0])) and (int(nums[i][1][1]) >= int(nums[i][0][1])):
        total += 1

print(total)