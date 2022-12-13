from queue import PriorityQueue

# Read input

with open("input12.txt") as f:
    ls = list(map(lambda l:list(l.strip()), f.readlines()))

m = len(ls)
n = len(ls[1])

for i in range(m):
    for j in range(n):
        if ls[i][j] == 'S':
            S = (i,j)
            ls[i][j] = 'a'
        if ls[i][j] == 'E':
            E = (i,j)
            ls[i][j] = 'z'

def neighbours(x,y):
    ns = []
    if x > 0 and ord(ls[x-1][y]) <= ord(ls[x][y])+1:
        ns.append((x-1,y))
    if x < m-1 and ord(ls[x+1][y]) <= ord(ls[x][y])+1:
        ns.append((x+1,y))
    if y > 0 and ord(ls[x][y-1]) <= ord(ls[x][y])+1:
        ns.append((x,y-1))
    if y < n-1 and ord(ls[x][y+1]) <= ord(ls[x][y])+1:
        ns.append((x,y+1))
    return(ns)

def hike(S):
    dist = [[10000 for _ in range(n)] for _ in range(m)]

    dist[S[0]][S[1]] = 0
    black = set([S])

    grey = PriorityQueue()
    for nd in neighbours(S[0],S[1]):
        grey.put((1,nd))

    while grey.qsize()>0:
        nd = grey.get()
        if nd[1] == E:
            return(nd[0])
        black.add(nd)

        for v in neighbours(nd[1][0],nd[1][1]):
            if v in black:
                continue
            if nd[0]+1 < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = nd[0]+1
                grey.put((nd[0]+1,v))
    return(10000)

# Part 1

print(hike(S))

# Part 2

minhike = 10000

for i in range(m):
    for j in range(n):
        if ls[i][j] == 'a':
            h = hike((i,j))
            if h < minhike:
                minhike = h

print(minhike)