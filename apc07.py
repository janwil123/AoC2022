from collections import defaultdict

# Read input

with open("input07.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

# Part 1&2

dirtree = {}
curdir = ()

i = 0 # The command index

while i < len(ls):
    cmd = ls[i].split()
    if cmd[0]=='$':
        if cmd[1]=='cd':
            if cmd[2]!='..':
                curdir += tuple([cmd[2]])
            else: # cd ..
                curdir = curdir[:-1]
        else: # cmd[1]=='ls'
            while (i+1 < len(ls)) and (ls[i+1].split()[0] != '$'):
                i += 1
                if ls[i].split()[0] != 'dir': 
                    if curdir in dirtree:
                        dirtree[curdir].append(ls[i].split())
                    else:
                        dirtree[curdir] = [ls[i].split()]
    i += 1

dtrs = sorted(dirtree,key=lambda a: len(a),reverse=True)

dirsizes = defaultdict(int)

for d in dtrs:
    for e in dirtree[d]:
        for i in range(1,len(d)+1):
            dirsizes[d[:i]] += int(e[0])

sum = 0
free = 70000000 - dirsizes[('/',)]
mindel = 70000000

for d in dirsizes:
    if dirsizes[d] <= 100000:
        sum += dirsizes[d]
    if (free + dirsizes[d]) >= 30000000:
        if dirsizes[d] < mindel:
            mindel = dirsizes[d]

print(sum)

print(mindel)