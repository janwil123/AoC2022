# Read input

with open("input04.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

# Part 1&2

duplicate = 0
nooverlap = 0

for l in ls:
    elf1,elf2 = l.split(',')
    e1l,e1r = map(int,elf1.split('-'))
    e2l,e2r = map(int,elf2.split('-'))
    if ((e1l <= e2l) and (e1r >= e2r)) or ((e1l >= e2l) and (e1r <= e2r)): 
        duplicate += 1
    if (e1r < e2l) or (e2r < e1l):
        nooverlap += 1


print(duplicate)
print(len(ls)-nooverlap)

