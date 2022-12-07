# Read input

with open("input06.txt") as f:
    l = f.readline().strip()

# Part 1

for i in range(len(l)-4):
    if len(set(l[i:i+4])) == 4:
        print(i+4)
        break

# Part 2

for i in range(len(l)-14):
    if len(set(l[i:i+14])) == 14:
        print(i+14)
        break