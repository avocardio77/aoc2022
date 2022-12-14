from anytree import Node, RenderTree
import numpy as np

file = open('aoc7input.txt')
lines = file.readlines()

dirs = {}
files = {}
root = Node('root', size = 0)
currentDir = root
dirs['root'] = root

def createTree():

    for line in lines:
        line = line.strip()
        splitLine = line.split(' ')

        if line == '$ cd /':
            currentDir = root
      #      print(line, 'root dir')

        elif line == '$ cd ..':
            try:
                currentDir = currentDir.parent
            except Exception as e:
                print(currentDir.name, 'has no parent!')
     #       print(line, 'change dir back')

        elif splitLine[0] == '$' and splitLine[1] == 'cd':
            newDirName = splitLine[2]
            currentDirChildren = [d.name for d in currentDir.children]
            newDirIndex = currentDirChildren.index(newDirName)
            currentDir = currentDir.children[newDirIndex]


        elif line == '$ ls':
            # print(line, 'list content')
            pass

        elif splitLine[0] == 'dir':
            newDirName = splitLine[1]
            if newDirName not in [d.name for d in currentDir.children]:
                newDir = Node(newDirName, parent = currentDir, size = 0)

        elif splitLine[0] != '$':
            fileName = splitLine[1]
            fileSize = splitLine[0]
            if fileName not in [f.name for f in currentDir.children]:
                # print(line, 'create file')
                file = Node(fileName, parent = currentDir, size = int(fileSize))

        else:
            print('something else')


def calcDirSize(x):
    dirSize = 0
    for desc in x.descendants:
        dirSize += int(desc.size)
    return dirSize

def dirsWithLimitedSize(limit):
    limitedDirs = []
    limitedDirsTotalSize = 0
    for dir in root.descendants:
        dirSize = calcDirSize(dir)
        if dirSize < limit:
            limitedDirs.append(dir)
            limitedDirsTotalSize += dirSize
    return limitedDirsTotalSize




createTree()

print(dirsWithLimitedSize(100000))

# part two

print(calcDirSize(root)) 

limit = 30_000_000 - (70_000_000-calcDirSize(root))
smallestGood = 10_000_000_000    

for item in root.descendants:
    fileSize = calcDirSize(item)
    if limit <= fileSize < smallestGood:
        smallestGood = fileSize

print(smallestGood)