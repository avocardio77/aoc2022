file = open('aoc4input.txt')
lines = file.readlines()

def fullyContains(firstPair, secondPair):
	firstPairSplit = [int(item) for item in firstPair.split('-')]
	secondPairSplit = [int(item) for item in secondPair.split('-')]

	if firstPairSplit[0] >= secondPairSplit[0] and firstPairSplit[1] <= secondPairSplit[1]:
		return True 
	elif secondPairSplit[0] >= firstPairSplit[0] and secondPairSplit[1] <= firstPairSplit[1]:
		return True
	else:
		return False

points = 0

for line in lines:
    line = line.strip()
    firstPair, secondPair = line.split(',')
    if fullyContains(firstPair, secondPair):
    	points += 1
print(points)

# part two

def partlyContains(firstPair, secondPair):
	firstPairSplit = [int(item) for item in firstPair.split('-')]
	secondPairSplit = [int(item) for item in secondPair.split('-')]

	if firstPairSplit[0] <= secondPairSplit[0] <= firstPairSplit[1]:
		return True 
	elif firstPairSplit[0] <= secondPairSplit[1] <= firstPairSplit[1]:
		return True
	elif firstPairSplit[0] <= secondPairSplit[0] <= secondPairSplit[1] <= firstPairSplit[1]:
		return True
	elif secondPairSplit[0] <= firstPairSplit[0] <= firstPairSplit[1] <= secondPairSplit[1]:
		return True
	else:
		print(firstPairSplit, secondPairSplit)
		return False

points = 0

for line in lines:
    line = line.strip()
    firstPair, secondPair = line.split(',')
    if partlyContains(firstPair, secondPair):
    	points += 1
print(points)