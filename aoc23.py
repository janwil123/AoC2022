# Read input

with open("input23.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

elves = set()

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == '#':
            elves.add((j,i))

dirs = [[(0,-1),(1,-1),(-1,-1)],[(0,1),(1,1),(-1,1)],
        [(-1,0),(-1,-1),(-1,1)],[(1,0),(1,-1),(1,1)]]

def al(v1,v2):  # Add locations function
    return((v1[0]+v2[0],v1[1]+v2[1]))

def printE():
    for i in range(len(ls)):
        line = ""
        for j in range(len(ls[0])):
            if (j,i) in elves:
                line+='#'
            else:
                line+='.'
        print(line)

ds = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def alone(elf):
    for d in ds:
        if al(elf,d) in elves:
            return(False)
    return(True)

    

# Part 1

for round in range(10):
    props = {}   # Proposed movements {move_to:move_from,...}
    dbl  = set() # Doubly proposed locations
    for elf in elves: # Elves consider moving
        if not(alone(elf)):
            for dir in dirs:
                if not(al(elf,dir[0]) in elves) and not(al(elf,dir[1]) in elves) and not(al(elf,dir[2]) in elves):
                    # The Elf proposes to move
                    if not(al(elf,dir[0]) in props):
                        props[al(elf,dir[0])] = elf 
                    else:
                        dbl.add(al(elf,dir[0]))
                    break
    for prop in props:
        if not(prop in dbl):
            elves.add(prop)
            elves.remove(props[prop])

    dirs = [dirs[1],dirs[2],dirs[3],dirs[0]]

minx,miny,maxx,maxy = 1000000,1000000,-1000000,-1000000

for elf in elves:
    if elf[0] < minx:
        minx = elf[0]
    if elf[1] < miny:
        miny = elf[1]
    if elf[0] > maxx:
        maxx = elf[0]
    if elf[1] > maxy:
        maxy = elf[1]

print((maxx-minx+1)*(maxy-miny+1)-len(elves))  

# Part 2

elves = set()

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == '#':
            elves.add((j,i))

dirs = [[(0,-1),(1,-1),(-1,-1)],[(0,1),(1,1),(-1,1)],
        [(-1,0),(-1,-1),(-1,1)],[(1,0),(1,-1),(1,1)]]

round = 1

while True:
    props = {}   # Proposed movements {move_to:move_from,...}
    dbl  = set() # Doubly proposed locations
    for elf in elves: # Elves consider moving
        if not(alone(elf)):
            for dir in dirs:
                if not(al(elf,dir[0]) in elves) and not(al(elf,dir[1]) in elves) and not(al(elf,dir[2]) in elves):
                    # The Elf proposes to move
                    if not(al(elf,dir[0]) in props):
                        props[al(elf,dir[0])] = elf 
                    else:
                        dbl.add(al(elf,dir[0]))
                    break
    move = False
    for prop in props:
        if not(prop in dbl):
            elves.add(prop)
            elves.remove(props[prop])
            move = True

    if not(move):
        print(f'First static round: {round}')
        break
    else:
        dirs = [dirs[1],dirs[2],dirs[3],dirs[0]]
        round += 1