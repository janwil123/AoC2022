# Read input

with open("input21.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

T = {}

for l in ls:
    s = l.split()
    if len(s) == 2:
        T[s[0][:-1]] = [int(s[1])]
    else:
        T[s[0][:-1]] = [s[2],s[1],s[3]]

# Part 1

def compute(node):
    ns = T[node]
    if isinstance(ns[0],int):
        return(ns[0])
    else:
        if ns[0] == '+':
            return(compute(ns[1])+compute(ns[2]))
        if ns[0] == '-':
            return(compute(ns[1])-compute(ns[2]))
        if ns[0] == '*':
            return(compute(ns[1])*compute(ns[2]))
        if ns[0] == '/':
            return(compute(ns[1])//compute(ns[2]))            

print(compute('root'))

# Part 2

def hasHuman(node):
    if node == 'humn':
        return(True)
    ns = T[node]
    if isinstance(ns[0],int):
        return(False)
    else:
        return(hasHuman(ns[1]) or hasHuman(ns[2]))

def computeH(node,res): # What the human has to yell in order to get the desired outcome from this subtree?
    if node == 'humn':
        return(res)
    ns = T[node]
    H1 = hasHuman(ns[1])
    H2 = hasHuman(ns[2])
    if H1: #Human is in the left subtree
        r = compute(ns[2])
        if ns[0] == '+':
            return(computeH(ns[1],res-r))
        if ns[0] == '-':
            return(computeH(ns[1],res+r))
        if ns[0] == '*':
            return(computeH(ns[1],res//r))
        if ns[0] == '/':
            return(computeH(ns[1],res*r)) 
    else: #Human is in the right subtree
        r = compute(ns[1])
        if ns[0] == '+':
            return(computeH(ns[2],res-r))
        if ns[0] == '-':
            return(computeH(ns[2],r-res))
        if ns[0] == '*':
            return(computeH(ns[2],res//r))
        if ns[0] == '/':
            return(computeH(ns[2],r//res)) 

H1 = T['root'][1]
H2 = T['root'][2]

if H1:
    M1,M2 = T['root'][1],T['root'][2]
else:
    M2,M1 = T['root'][1],T['root'][2]

# Now M1 has human in its tree and M2 does not

res = compute(M2)

print(computeH(M1,res))
