from copy import deepcopy

# Read input

with open("input11.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

monkeys = (len(ls)+1)//7

items = []

for i in range(monkeys):
    s = ls[7*i+1]
    t = s.split(':')[1]
    items.append(list(map(int,t.split(','))))

# Retain the items for Part 2
items2 = deepcopy(items)
    
ops = []

for i in range(monkeys):
    s = ls[7*i+2]
    t = s.split('=')[1]    
    ops.append(t.split())

tests = []

for i in range(monkeys):
    s = ls[7*i+3]
    t = int(s.split()[-1])    
    s = ls[7*i+4]
    u = int(s.split()[-1])        
    s = ls[7*i+5]
    v = int(s.split()[-1])     
    tests.append([t,u,v])

mod = 1
for t in tests:
    mod *= t[0]

# Part 1

def newlevel1(level,op):
    if op[-1] == 'old': # We have old * old
        nl = level*level
    else: # We have an op with a constant
        n = int(op[-1])
        if op[-2] == '+':
            nl = level + n
        else: # op[-2] == '*'
            nl = level * n
    nl = nl//3

    return(nl)

inspect = [0 for _ in range(monkeys)]

for r in range(20):
    for m in range(monkeys):
        for i in items[m]:
            inspect[m] += 1
            level = newlevel1(i,ops[m])
            if level%tests[m][0] == 0:
                items[tests[m][1]].append(level)
            else:
                items[tests[m][2]].append(level)
        items[m] = []

inspect.sort()

print(inspect[-1]*inspect[-2])

# Part 2

def newlevel2(level,op):
    if op[-1] == 'old': # We have old * old
        nl = (level*level)%mod
    else: # We have an op with a constant
        n = int(op[-1])
        if op[-2] == '+':
            nl = (level + n)%mod
        else: # op[-2] == '*'
            nl = (level * n)%mod

    return(nl)

inspect = [0 for _ in range(monkeys)]

for r in range(10000):
    for m in range(monkeys):
        for i in items2[m]:
            inspect[m] += 1
            level = newlevel2(i,ops[m])
            if level%tests[m][0] == 0:
                items2[tests[m][1]].append(level)
            else:
                items2[tests[m][2]].append(level)
        items2[m] = []

inspect.sort()

print(inspect[-1]*inspect[-2])