import numpy as np

forestWidth = 99
forestHeight = 99

forest = []
visibleTrees = np.zeros((forestWidth, forestHeight))

with open('aoc8input.txt') as f:
    for line in f:
        forest.append([int(x) for x in line[:forestWidth]])

forest = np.array(forest)

# left to right

for i in range(forestHeight):
    rowCumMaxHeight = -1
    for j in range(forestWidth):
        if forest[i,j] > rowCumMaxHeight:
            rowCumMaxHeight = forest[i,j]
            visibleTrees[i,j] = 1
    rowCumMaxHeight = 0

# right to left

for i in reversed(range(forestHeight)):
    rowCumMaxHeight = -1
    for j in reversed(range(forestWidth)):
        if forest[i,j] > rowCumMaxHeight:
            rowCumMaxHeight = forest[i,j]
            visibleTrees[i,j] = 1
    rowCumMaxHeight = 0

# up to down

for i in range(forestHeight):
    rowCumMaxHeight = -1
    for j in range(forestWidth):
        if forest[j,i] > rowCumMaxHeight:
            rowCumMaxHeight = forest[j,i]
            visibleTrees[j,i] = 1
    rowCumMaxHeight = 0

# down to up

for i in reversed(range(forestHeight)):
    rowCumMaxHeight = -1
    for j in reversed(range(forestWidth)):
        if forest[j,i] > rowCumMaxHeight:
            rowCumMaxHeight = forest[j,i]
            visibleTrees[j,i] = 1
    rowCumMaxHeight = 0

print(np.sum(visibleTrees))