import sys
sys.setrecursionlimit(15000)

# Read input

with open("input18.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

cubes = set()
ma = 0
for l in ls:
    x,y,z = map(int,l.split(','))
    cubes.add((x+1,y+1,z+1))
    if max(x+1,y+1,z+1) > ma:
        ma = max(x+1,y+1,z+1)

def countsides(cubeset):
    sides = set()

    for cube in cubeset:
        (x,y,z) = cube
        if (x+1,y,z,'L') in sides:
            sides.remove((x+1,y,z,'L'))
        else:
            sides.add((x,y,z,'R'))
        if (x-1,y,z,'R') in sides:
            sides.remove((x-1,y,z,'R'))
        else:
            sides.add((x,y,z,'L'))    

        if (x,y+1,z,'B') in sides:
            sides.remove((x,y+1,z,'B'))
        else:
            sides.add((x,y,z,'F'))
        if (x,y-1,z,'F') in sides:
            sides.remove((x,y-1,z,'F'))
        else:
            sides.add((x,y,z,'B'))

        if (x,y,z+1,'D') in sides:
            sides.remove((x,y,z+1,'D'))
        else: 
            sides.add((x,y,z,'U'))
        if (x,y,z-1,'U') in sides:
            sides.remove((x,y,z-1,'U'))
        else: 
            sides.add((x,y,z,'D'))

    return(len(sides))

# Part 1

print(countsides(cubes))

# Part 2

dim = ma+2

def neighbours(cube):
    res = []
    (x,y,z) = cube
    if x > 0:
        res.append((x-1,y,z))
    if x < dim-1:
        res.append((x+1,y,z))
    if y > 0:
        res.append((x,y-1,z))
    if y < dim-1:
        res.append((x,y+1,z))
    if z > 0:
        res.append((x,y,z-1))
    if z < dim-1:
        res.append((x,y,z+1))
    return(res)

visited = set()

def dfs(cube):
    visited.add(cube)
    for n in neighbours(cube):
        if not(n in visited) and not(n in cubes):
            dfs(n)

d = dfs((0,0,0))

print(countsides(visited)-6*dim*dim)