# Read input

with open("input10.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

# Part 1

X = 1
steps = 0
total = 0

for l in ls:
    cmd = l.split()
    if cmd[0] == 'noop':
        steps += 1
        if steps%40 == 20:
            total += steps*X    
    else: # cmd[0] == 'addx'
        a = int(cmd[1])
        steps += 1
        if steps%40 == 20:
            total += steps*X
        steps += 1
        if steps%40 == 20:
            total += steps*X
        X += a

print(total)        

# Part 2

X = 1
steps = 0
line = ""

for l in ls:
    cmd = l.split()
    if cmd[0] == 'noop':
        steps += 1
        if abs(X-((steps-1)%40)) <=1:
            line+='#'
        else:
            line+='.'
        if steps%40 == 0:
            print(line)
            line = ""
    else: # cmd[0] == 'addx'
        a = int(cmd[1])
        steps += 1
        if abs(X-((steps-1)%40)) <=1:
            line+='#'
        else:
            line+='.'
        if steps%40 == 0:
            print(line)
            line = ""
        steps += 1
        if abs(X-((steps-1)%40)) <=1:
            line+='#'
        else:
            line+='.'
        if steps%40 == 0:
            print(line)
            line = "" 
        X += a
