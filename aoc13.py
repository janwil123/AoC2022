# Read input

with open("input13.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))


def cmpr(l1,l2):
    if type(l1) is list and type(l2) is list:
        if len(l1) == 0 and len(l2) == 0:
            return('Equal') 
        if len(l1) == 0:
            return(True)
        if len(l2) == 0:
            return(False)
        res = cmpr(l1[0],l2[0])
        if res == True or res == False:
            return(res)
        else:
            return(cmpr(l1[1:],l2[1:]))
    if type(l1) is list and type(l2) is int:
        return(cmpr(l1,[l2]))
    if type(l1) is int and type(l2) is list:
        return(cmpr([l1],l2))
    if type(l1) is int and type(l2) is int:
        if l1 < l2:
            return(True)
        if l1 > l2:
            return(False)    
        return('Equal')

# Part 1

s = 0

for i in range((len(ls)+1)//3):
    l1 = eval(ls[3*i])
    l2 = eval(ls[3*i+1])
    if cmpr(l1,l2):
        s += (i+1)

print(s)

# Part 2

def sortL(L):
    if len(L) <= 1:
        return(L)
    L1 = L[:len(L)//2]
    L2 = L[len(L)//2:]
    L1 = sortL(L1)
    L2 = sortL(L2)
    Lr = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if cmpr(L1[i],L2[j]):
            Lr.append(L1[i])
            i += 1
        else:
            Lr.append(L2[j])
            j += 1
    if i == len(L1):
        Lr += L2[j:]
    else:
        Lr += L1[i:]
    return(Lr)

L = []

for i in range((len(ls)+1)//3):
    L.append(eval(ls[3*i]))
    L.append(eval(ls[3*i+1]))
L.append([[2]])
L.append([[6]])

L = sortL(L)

for i in range(len(L)):
    if L[i] == [[2]]:
        a = i+1
    if L[i] == [[6]]:
        b = i+1

print(a*b)