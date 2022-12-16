import numpy as np

X = 1
round = 0
queue = []

waitTime = 0

    

with open('aoc10input.txt') as f:
    for line in f:
        line = line.strip()
        command = line.strip().split(' ')[0]
        if command == 'noop':
            queue.insert(len(queue), [command, waitTime + 1])
            waitTime += 1
        elif command == 'addx':
            queue.insert(len(queue), [line, waitTime + 2])
            waitTime += 2
        queue = [[i[0], i[1]-1] for i in queue]
        print('wait time: ', queue[0][1])
        while(True):
            firstItem = queue[0]
            if firstItem[1] != 0:
                break
            if firstItem[0] == 'noop':
                queue.pop()
                print('moi1')
            else:
                queue.pop()
                print('moi2')
        round += 1

print(queue)