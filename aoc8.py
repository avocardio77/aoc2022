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

# part two

forest = []
scenicScores = np.zeros((forestWidth, forestHeight))

with open('aoc8input.txt') as f:
    for line in f:
        forest.append([int(x) for x in line[:forestWidth]])

forest = np.array(forest)

for i in range(forestHeight):
    for j in range(forestWidth):
        scenicScoreDown = 0
        while(True):
            try:
                nextTree = forest[i+scenicScoreDown+1,j]
                if nextTree >= forest[i,j]:
                    scenicScoreDown += 1
                    break
                else:
                    scenicScoreDown += 1
            except Exception as e:
                break

        scenicScoreRight = 0
        while(True):
            try:
                nextTree = forest[i,j+scenicScoreRight+1]
                if nextTree >= forest[i,j]:
                    scenicScoreRight += 1
                    break
                else:
                    scenicScoreRight += 1
            except Exception as e:
                break

        scenicScoreLeft = 0
        while(j-scenicScoreLeft-1 >= 0):
            try:
                nextTree = forest[i,j-scenicScoreLeft-1]
                if nextTree >= forest[i,j]:
                    scenicScoreLeft += 1
                    break
                else:
                    scenicScoreLeft += 1
            except Exception as e:
                break

        scenicScoreUp = 0
        while(i-scenicScoreUp-1 >= 0):
            try:
                nextTree = forest[i-scenicScoreUp-1,j]
                if nextTree >= forest[i,j]:
                    scenicScoreUp += 1
                    break
                else:
                    scenicScoreUp += 1
            except Exception as e:
                break
        scenicScores[i,j] = scenicScoreRight*scenicScoreLeft*scenicScoreUp*scenicScoreDown

print(np.max(scenicScores))