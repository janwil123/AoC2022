# Read input

with open("input09.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

d = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

def newcell(Hx,Hy,Tx,Ty):
    if abs(Hx-Tx) <= 1 and abs(Hy-Ty) <= 1:
        return((Tx,Ty))
    if Hx>Tx and Hy>Ty:
        return((Tx+1,Ty+1))
    if Hx>Tx and Hy<Ty:
        return((Tx+1,Ty-1))
    if Hx<Tx and Hy>Ty:
        return((Tx-1,Ty+1))
    if Hx<Tx and Hy<Ty:
        return((Tx-1,Ty-1))
    if Hx==Tx+2:
        return((Tx+1,Ty))
    if Hx==Tx-2:
        return((Tx-1,Ty))    
    if Hy==Ty+2:
        return((Tx,Ty+1))
    if Hy==Ty-2:
        return((Tx,Ty-1))    

def walk(ropelen):
    rope = [(0,0) for _ in range(ropelen)]

    cells = set()

    for l in ls:
        dir = l.split()[0]
        n   = int(l.split()[1])
        for _ in range(n):
            rope[0] = (rope[0][0]+d[dir][0],rope[0][1]+d[dir][1])
            for i in range(1,ropelen):
                rope[i] = newcell(rope[i-1][0],rope[i-1][1],rope[i][0],rope[i][1])
            cells.add(rope[-1])
    
    return(len(cells))

# Part 1 

print(walk(2))

# Part 2

print(walk(10))