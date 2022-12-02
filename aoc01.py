# Read input

with open("input01.txt") as f:
    ns = f.readlines()

# Part 1

maxcnt = 0
cnt = 0

for l in ns:
    if l == '\n':
        if cnt>maxcnt:
            maxcnt = cnt
        cnt = 0

    else:
        cnt += int(l)

print(maxcnt)

# Part 2

cnts = []

cnt = 0

for l in ns:
    if l == '\n':
        cnts.append(cnt)
        cnt = 0

    else:
        cnt += int(l)

cnts.sort()

print(cnts[-1]+cnts[-2]+cnts[-3])