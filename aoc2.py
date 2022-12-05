sum = 0
max = 0

with open('C:/Users/routa/Documents/aoc/aoc1input.txt') as f:
    for line in f:
        if line != '\n':
            sum += int(line)
        else:
            if sum > max:
                    max = sum
            sum = 0

print(max)