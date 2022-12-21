from copy import deepcopy

# Read input

with open("input20.txt") as f:
    ls = list(map(int, f.readlines()))

n = len(ls)
zi = ls.index(0)

lst = []

for i in range(n):
    lst.append([ls[i],(i-zi)%n])

lst2 = deepcopy(lst) # Retain the list for part 2

# Part 1

for l in lst:
    if l[0]==0:
        continue
    newpos = (l[0]+l[1])%(n-1)
    if newpos == 0:
        newpos = n-1
    if newpos > l[1]:
        for m in lst:
            if newpos >= m[1] > l[1]:
                m[1]-=1
        l[1] = newpos

    if newpos < l[1]:
        for m in lst:
            if newpos <= m[1] < l[1]:
                m[1]+=1
        l[1] = newpos        
    

s = 0

for l in lst:
    if l[1] in [1000%n,2000%n,3000%n]:
        s += l[0]

print(s)

# Part 2

lst = lst2

for l in lst:
    l[0] = l[0]*811589153


for _ in range(10):
    for l in lst:
        if l[0]==0:
            continue
        newpos = (l[0]+l[1])%(n-1)
        if newpos == 0:
            newpos = n-1
        if newpos > l[1]:
            for m in lst:
                if newpos >= m[1] > l[1]:
                    m[1]-=1
            l[1] = newpos

        if newpos < l[1]:
            for m in lst:
                if newpos <= m[1] < l[1]:
                    m[1]+=1
            l[1] = newpos 

s = 0

for l in lst:
    if l[1] in [1000%n,2000%n,3000%n]:
        s += l[0]

print(s)