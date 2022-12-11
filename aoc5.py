import numpy as np
import math

file = open('aoc5input.txt')
lines = file.readlines()
stacks = {}

for line in lines:
    #line = line.strip()
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stack = math.ceil(i/4)
            try:
                stacks[stack].insert(0, line[i])
            except:
                stacks[stack] = [line[i]]

#print(stacks)

file2 = open('aoc5input2.txt')
lines2 = file2.readlines()

ans = ''

for line in lines2:
    splitLine = line.strip().split(' ')
    count, start, end = int(splitLine[1]), int(splitLine[3]), int(splitLine[5])
    for i in range(count):
        try:
            stacks[end].append(stacks[start].pop())
        except:
            stacks[end] = [stacks[start].pop()]

for i in range(1,10):
    ans += stacks[i].pop()
print(ans)
#print(stacks)

# part 2 --------------------------------------------------------------

file = open('aoc5input.txt')
lines = file.readlines()
stacks = {}

for line in lines:
    #line = line.strip()
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stack = math.ceil(i/4)
            try:
                stacks[stack].insert(0, line[i])
            except:
                stacks[stack] = [line[i]]

#print(stacks)

file2 = open('aoc5input2.txt')
lines2 = file2.readlines()

ans = ''

for line in lines2:
    splitLine = line.strip().split(' ')
    count, start, end = int(splitLine[1]), int(splitLine[3]), int(splitLine[5])
    tempStack = []

    for i in range(count):
        tempStack.append(stacks[start].pop())

    for i in range(count):
        try:
            stacks[end].append(tempStack.pop())
        except:
            stacks[end] = [tempStack.pop()]

for i in range(1,10):
    ans += stacks[i].pop()
print(ans)
#print(stacks)