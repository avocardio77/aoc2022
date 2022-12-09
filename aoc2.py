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
    elif ((opponent == 'A' and you == 'Y') or
                (opponent == 'B'and you == 'Z') or
                (opponent == 'C'and you == 'X')):
        return 6
    else:
        return 0


with open('aoc2input.txt') as f:
    for line in f:
        opponent = line.strip()[0]
        you = line.strip()[-1]
        pointsForRound = defineWinnerPoints(opponent, you) + outcomeScoreDict.get(you)
        sum += pointsForRound

print(sum)

sum = 0

# part two

abcXyz = {
    'Rock' : 'A',
    'Paper' : 'B',
    'Scissors' : 'C'
}

def win(opponent):
    if opponent == abcXyz.get('Rock'):
        return abcXyz.get('Paper')
    elif opponent == abcXyz.get('Paper'):
        return abcXyz.get('Scissors')
    else:
        return abcXyz.get('Rock')

def lose(opponent):
    if opponent == abcXyz.get('Rock'):
        return abcXyz.get('Scissors')
    elif opponent == abcXyz.get('Paper'):
        return abcXyz.get('Rock')
    else:
        return abcXyz.get('Paper')

def draw(opponent):
    return opponent

with open('aoc2input.txt') as f:
    for line in f:
        opponent = line.strip()[0]
        outcome = line.strip()[-1]
        if outcome == 'Y':
            you = draw(opponent)
        elif outcome == 'X':
            you = lose(opponent)
        else:
            you = win(opponent)
        you = rpsDict.get(you)
        print(defineWinnerPoints(opponent, you))
        print(outcomeScoreDict.get(you))
        pointsForRound = defineWinnerPoints(opponent, you) + outcomeScoreDict.get(you)


        print(f'you: {you}, opponent: {opponent}, pointsForRound: {pointsForRound}')


        sum += pointsForRound

print(sum)