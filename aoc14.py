from copy import deepcopy

# Read input

with open("input14.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

maxy = 169
dx = 300

M = [['.' for _ in range(2*(500-dx))] for _ in range(maxy+3)]

for l in ls:
    cs = l.split(' -> ')
    for i in range(len(cs)-1):
        x1,y1 = map(int,cs[i].split(','))
        x2,y2 = map(int,cs[i+1].split(','))
        x1 -= dx
        x2 -= dx
        if x1==x2:
            if y1<y2:
                for y in range(y1,y2+1):
                    M[y][x1] = '#'
            else: # y2<y1
                for y in range(y2,y1+1):
                    M[y][x1] = '#'  
        else:# y1==y2
            if x1<x2:
                for x in range(x1,x2+1):
                    M[y1][x] = '#'
            else: # x2<x1
                for x in range(x2,x1+1):
                    M[y1][x] = '#' 

M2 = deepcopy(M) # Retain the map for part 2             

# Part1

cnt = 0
x = 500-dx
y = 0
M[y][x] = 'o'

while True:
    if M[y+1][x] == '.':
        M[y][x] = '.'
        y += 1
        M[y][x] = 'o'
        if y==maxy+2:
            break
        else:
            continue
    elif M[y+1][x-1] == '.':
        M[y][x] = '.'
        x -= 1
        y += 1
        M[y][x] = 'o'
        if y==maxy+2:
            break
        else:
            continue
    elif M[y+1][x+1] == '.':
        M[y][x] = '.'
        x += 1
        y += 1
        M[y][x] = 'o'
        if y==maxy+2:
            break   
        else:
            continue  
    x = 500-dx
    y = 0    
    M[y][x] = 'o'
    cnt += 1

print(cnt)

# Part 2

M = M2 # Restore the map from copy

M[maxy+2] = ['#' for _ in range(2*(500-dx))]

cnt = 1
x = 500-dx
y = 0
M[y][x] = 'o'

while True:
    if M[y+1][x] == '.':
        M[y][x] = '.'
        y += 1
        M[y][x] = 'o'
        continue
    elif M[y+1][x-1] == '.':
        M[y][x] = '.'
        x -= 1
        y += 1
        M[y][x] = 'o'
        continue
    elif M[y+1][x+1] == '.':
        M[y][x] = '.'
        x += 1
        y += 1
        M[y][x] = 'o'
        continue  
    if y > 0:
        x = 500-dx
        y = 0    
        M[y][x] = 'o'
        cnt += 1 
        continue
    else:
        break

print(cnt)