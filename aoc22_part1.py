# Read input

with open("input22.txt") as f:
    M = f.readlines()

commandline = 'R'+M[-1].rstrip()

M = list(map(lambda l:l.rstrip(), M[:-2]))

commands = []

for c in commandline:
    if c in ['R','L']:
        commands.append([c,0])
    else:
        commands[-1][1] = 10*commands[-1][1] + int(c)

y = 0
x = len(M[0])-len(M[0].strip())

dir = 3 # is 0 for right, 1 for down, 2 for left, and 3 for up 

for com in commands:
    if com[0]== 'R':
        dir = (dir+1)%4
    else:
        dir = (dir-1)%4
    if dir == 0: # Right
        for i in range(com[1]):
            if x == len(M[y])-1: # We are at the right end
                x1 = len(M[y])-len(M[y].strip())
                if M[y][x1] == '#': # Can we go around?
                    break
                else:
                    x = x1
                    continue
            if M[y][x+1] == '#': # Are we facing a rock?
                break
            else:
                x += 1
    if dir == 2: # Left
        for i in range(com[1]):
            if x == 0 or x == len(M[y])-len(M[y].strip()): # We are at the left end
                x1 = len(M[y])-1
                if M[y][x1] == '#': # Can we go around?
                    break
                else:
                    x = x1
                    continue
            if M[y][x-1] == '#': # Are we facing a rock?
                break
            else:
                x -= 1     
    if dir == 1: # Down
        for i in range(com[1]):
            if y == len(M)-1 or len(M[y+1]) <= x or M[y+1][x] == ' ': # We are at the bottom
                for y1 in range(y):
                    if M[y1][x] != ' ':
                        break # Now y1 is the row where we should reappear
                if M[y1][x] == '#': # Can we go around?
                    break
                else:
                    y = y1
                    continue
            if M[y+1][x] == '#': # Are we facing a rock?
                break
            else: 
                y += 1
    if dir == 3: # Up
        for i in range(com[1]):
            if y == 0 or len(M[y-1]) <= x or M[y-1][x] == ' ': # We are at the top
                y1 = y
                while True:
                    if y1+1< len(M) and len(M[y1+1]) > x and M[y1+1][x] != ' ':
                        y1 += 1
                    else:
                        break
                # Now y1 is the bottom where we can reappear
                if M[y1][x] == '#': # Can we go around?
                    break
                else:
                    y = y1
                    continue
            if M[y-1][x] == '#': # Are we facing a rock?
                break
            else: 
                y -= 1                

print(1000*(y+1)+4*(x+1)+dir)

