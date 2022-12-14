file = open('aoc6input.txt')
line = file.readlines()[0]
print(line)

count = 0
while True:
	 chars = ''.join(set(line[count:count+4]))
	 if len(chars) == 4:
	 	print(int(count) + 4)
	 	break
	 else:
	 	count += 1

# part two

count = 0
while True:
	 chars = ''.join(set(line[count:count+14]))
	 if len(chars) == 14:
	 	print(int(count) + 14)
	 	break
	 else:
	 	count += 1