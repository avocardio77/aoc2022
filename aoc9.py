import numpy as np

DIR = {
    'U': np.array([-1,0]),
    'D': np.array([1, 0]),
    'R': np.array([0, 1]),
    'L': np.array([0,-1])
}

headCoord = np.array([0,0])
tailCoord = np.zeros(2)

tailTrail = [[0,0]]

def move(pos1, pos2):
        new_pos2 = pos2
        if np.abs(pos1[0] - pos2[0]) == 2:
            new_pos2[0] = int(np.mean([pos1[0],pos2[0]]))
            if np.abs(pos1[1] - pos2[1]) == 1:
                new_pos2[1] = pos1[1]
            elif np.abs(pos1[1] - pos2[1]) == 2:
                new_pos2[1] = int(np.mean([pos1[1],pos2[1]]))
        if np.abs(pos1[1] - pos2[1]) == 2:
            new_pos2[1] = np.mean([pos1[1],pos2[1]])
            if np.abs(pos1[0] - pos2[0]) == 1:
                new_pos2[0] = pos1[0]
            elif np.abs(pos1[0] - pos2[0]) == 2:
                new_pos2[0] = int(np.mean([pos1[0],pos2[0]]))
        return(new_pos2)

with open('aoc9input.txt') as f:
    for line in f:
        dir = line.split(' ')[0]
        count = int(line.split(' ')[1])
        for i in range(count):
            headCoord += DIR.get(dir)
            tailCoord = move(headCoord, tailCoord)
            tailTrail = np.append(tailTrail, [tailCoord], axis = 0)
            
print(len(np.unique(tailTrail, axis = 0)))

# part two

headCoord = np.array([0,0])
tailCoord = np.zeros([9, 2])


tailTrail = [[0,0]]

with open('aoc9input.txt') as f:
    for line in f:
        dir = line.split(' ')[0]
        count = int(line.split(' ')[1])
        for i in range(count):
            headCoord += DIR.get(dir)
            tailCoord[0] = move(headCoord, tailCoord[0])
            for tailPart in range(1,9):
                tailCoord[tailPart] = move(tailCoord[tailPart-1], tailCoord[tailPart])
            tailTrail = np.append(tailTrail, [tailCoord[-1]], axis = 0)
            #tailTrail = np.unique(tailTrail, axis = 0)
            
#print(tailTrail)
print(len(np.unique(tailTrail, axis = 0)))