sum = 0

rpsDict = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

outcomeScoreDict = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

def defineWinnerPoints(opponent, you):
    if (rpsDict.get(opponent) == you):
        return 3
    elif ((opponent == 'A' & you == 'Y') |
                (opponent == 'B' & you == 'Z') |
                (opponent == 'C' & you == 'X')):
        return 6
    else:
        return 0


with open('aoc2input.txt') as f:
    for line in f:
        print(line)