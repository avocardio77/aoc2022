import numpy as np

sum = 0
max = 0

with open('aoc1input.txt') as f:
    for line in f:
        if line != '\n':
            sum += int(line)
        else:
            if sum > max:
                    max = sum
            sum = 0

print(max)

sum = 0
lst = []

with open('aoc1input.txt') as f:
    for line in f:
        if line != '\n':
            sum += int(line)
        else:
            lst.append(sum)
            sum = 0

print(np.sum(sorted(lst)[-3:]))