# Read input

with open("input22.txt") as f:
    ls = list(map(lambda l:l[:-1], f.readlines()))

sidelen = 50

# Transform command line

commandline = 'R'+ls[-1]
cmd = ''
n = 0

for c in commandline:
    if c in ['R','L']:
        cmd += 'F'*n
        cmd += c
        n = 0
    else:
        n = 10*n + int(c)

cmd += 'F'*n

# Prepare the data of faces

def rotM(mat): # Rotate the matrix left
    res = []
    for i in range(len(mat[0])):
        l = []
        for j in range(len(mat)):
            l.append(mat[j][len(mat[0])-1-i])
        res.append(l)
    return(res)


def printM(mat):
    for l in mat:
        print(''.join(l))

class Face():
    def __init__(self,id,M,sides):
        self.id = id
        self.M = M
        self.sides = sides

faces = {}

# Read the upper face

M = []

for i in range(0*sidelen,1*sidelen):
    row = []
    for j in range(1*sidelen,2*sidelen):
        row.append(ls[i][j])
    M.append(row)

sides = {}

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('U',M,sides)

faces['U'] = newFace

# Read the back face

M = []

for i in range(1*sidelen,2*sidelen):
    row = []
    for j in range(1*sidelen,2*sidelen):
        row.append(ls[i][j])
    M.append(row)

sides = {}

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('B',M,sides)

faces['B'] = newFace

# Read the down face

M = []

for i in range(2*sidelen,3*sidelen):
    row = []
    for j in range(1*sidelen,2*sidelen):
        row.append(ls[i][j])
    M.append(row)

sides = {}

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('D',M,sides)

faces['D'] = newFace

# Read the left face

M = []

for i in range(2*sidelen,3*sidelen):
    row = []
    for j in range(0*sidelen,1*sidelen):
        row.append(ls[i][j])
    M.append(row)

sides = {}

M = rotM(rotM(rotM(M)))

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('L',M,sides)

faces['L'] = newFace

# Read the front face

M = []

for i in range(3*sidelen,4*sidelen):
    row = []
    for j in range(0*sidelen,1*sidelen):
        row.append(ls[i][j])
    M.append(row)

sides = {}

M = rotM(rotM(rotM(M)))

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('F',M,sides)

faces['F'] = newFace

# Read the right face

M = []

for i in range(0*sidelen,1*sidelen):
    row = []
    for j in range(2*sidelen,3*sidelen):
        row.append(ls[i][j])
    M.append(row)

M = rotM(rotM(rotM(M))) 

sides = {}

sides['U'] = M[0]
M = rotM(M)
sides['R'] = M[0]
M = rotM(M)
sides['D'] = M[0]
M = rotM(M)
sides['L'] = M[0]
M = rotM(M)

newFace = Face('R',M,sides)

faces['R'] = newFace

# Initialise the trail

neighbour = {'UL':'LU','UU':'FU','UR':'RU','UD':'BU',
             'BL':'LR','BU':'UD','BR':'RL','BD':'DU',
             'DL':'LD','DU':'BD','DR':'RD','DD':'FD',
             'LL':'FR','LU':'UL','LR':'BL','LD':'DL',
             'FL':'RR','FU':'UU','FR':'LL','FD':'DD',
             'RL':'BR','RU':'UR','RR':'FL','RD':'DR'}

def rotL(v):        # Rotate vector left
    return((v[1],-v[0]))

def rotR(v):        # Rotate vector right
    return((-v[1],v[0]))

cf = 'U' # Current face
x,y = 0,0  # Coordinates on the current face
dir = (0,-1) # The original direction is up which is turned right right away

# Go through the trail

for c in cmd:
    if c == 'R':
        dir = rotR(dir)
    elif c == 'L':
        dir = rotL(dir)
    else: # c == 'F', i.e. we go a step forward
        x1 = x+dir[0]   # Potential new coordinates
        y1 = y+dir[1]
        if (0 <= x1 < sidelen) and (0 <= y1 < sidelen): # We would stay on the face
            if faces[cf].M[y1][x1] == '.': # We can move 
                x,y = x1,y1
        else: # We would step outside
            if x1 == -1:
                ns = neighbour[cf+'L']  # New side
                np = y                  # New position on the new side
                if (faces[ns[0]].sides[ns[1]])[np] != '#': # The step is not blocked
                    cf = ns[0]
                    if ns[1] == 'U':
                        x,y = np,0
                        dir = (0,1)
                    elif ns[1] == 'L':
                        x,y = 0,sidelen-1-np
                        dir = (1,0)
                    elif ns[1] == 'D':
                        x,y = sidelen-1-np, sidelen-1
                        dir = (0,-1)
                    elif ns[1] == 'R':
                        x,y = sidelen-1,np
                        dir = (-1,0)
            elif x1 == sidelen:
                ns = neighbour[cf+'R']  # New side
                np = sidelen-1-y        # New position on the new side
                if (faces[ns[0]].sides[ns[1]])[np] != '#': # The step is not blocked
                    cf = ns[0]
                    if ns[1] == 'U':
                        x,y = np,0
                        dir = (0,1)
                    elif ns[1] == 'L':
                        x,y = 0,sidelen-1-np
                        dir = (1,0)
                    elif ns[1] == 'D':
                        x,y = sidelen-1-np, sidelen-1
                        dir = (0,-1)
                    elif ns[1] == 'R':
                        x,y = sidelen-1,np
                        dir = (-1,0)
            elif y1 == -1:
                ns = neighbour[cf+'U']  # New side
                np = sidelen-1-x        # New position on the new side
                if (faces[ns[0]].sides[ns[1]])[np] != '#': # The step is not blocked
                    cf = ns[0]
                    if ns[1] == 'U':
                        x,y = np,0
                        dir = (0,1)
                    elif ns[1] == 'L':
                        x,y = 0,sidelen-1-np
                        dir = (1,0)
                    elif ns[1] == 'D':
                        x,y = sidelen-1-np, sidelen-1
                        dir = (0,-1)
                    elif ns[1] == 'R':
                        x,y = sidelen-1,np
                        dir = (-1,0)
            elif y1 == sidelen:
                ns = neighbour[cf+'D']  # New side
                np = x                  # New position on the new side
                if (faces[ns[0]].sides[ns[1]])[np] != '#': # The step is not blocked
                    cf = ns[0]
                    if ns[1] == 'U':
                        x,y = np,0
                        dir = (0,1)
                    elif ns[1] == 'L':
                        x,y = 0,sidelen-1-np
                        dir = (1,0)
                    elif ns[1] == 'D':
                        x,y = sidelen-1-np, sidelen-1
                        dir = (0,-1)
                    elif ns[1] == 'R':
                        x,y = sidelen-1,np
                        dir = (-1,0)              
    
print(f'Face {cf}, x={x}, y={y}, direction={dir}')