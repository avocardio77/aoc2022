file = open('aoc3input.txt')
lines = file.readlines()

prio = {'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,
        'A':27,
        'B':28,
        'C':29,
        'D':30,
        'E':31,
        'F':32,
        'G':33,
        'H':34,
        'I':35,
        'J':36,
        'K':37,
        'L':38,
        'M':39,
        'N':40,
        'O':41,
        'P':42,
        'Q':43,
        'R':44,
        'S':45,
        'T':46,
        'U':47,
        'V':48,
        'W':49,
        'X':50,
        'Y':51,
        'Z':52}

points = 0

for line in lines:
    line = line.strip()
    lineLength = len(line)
    firstHalf = line[:(int(lineLength/2))]
    lastHalf = line[int(lineLength/2):]
    letter = list(set(firstHalf)&set(lastHalf))[0]
    points += prio.get(letter)

print(points)

# part two

points = 0
multiplier = 0

while multiplier < 299:
    threeLines = [item.strip() for item in lines[multiplier:multiplier+3]]
    letter = list(set(threeLines[0])&set(threeLines[1])&set(threeLines[2]))[0]
    points += prio.get(letter)
    multiplier += 3

print(points)