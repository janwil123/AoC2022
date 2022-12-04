# Read input

with open("input03.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

# Part 1

res = 0

for l in ls:
    S1 = set(l[:len(l)//2])
    S2 = set(l[len(l)//2:])
    c = list(S1.intersection(S2))[0]
    if ord(c)>=97:
        res += (ord(c)-96)
    else:
        res += (ord(c)-64+26)

print(res)

# Part 2

res = 0

for i in range(len(ls)//3):
    S1 = set(ls[3*i])
    S2 = set(ls[3*i+1])
    S3 = set(ls[3*i+2])
    S4 = S1.intersection(S2)
    c = list(S3.intersection(S4))[0]
    if ord(c)>=97:
        res += (ord(c)-96)
    else:
        res += (ord(c)-64+26)

print(res)
