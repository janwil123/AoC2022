from copy import deepcopy

# Read input

with open("input05.txt") as f:
    ls = f.readlines()

numcrates = 9
depcrates = 8

state = []

for i in range(numcrates):
    crate = []
    for j in range(depcrates):
        if ls[j][4*i+1] != ' ':
            crate.append(ls[j][4*i+1])
    state.append(crate)

state2 = deepcopy(state) # Retain the original state for Part 2

# Part 1

for i in range(depcrates+2,len(ls)):
    cmd = ls[i].strip().split()
    n = int(cmd[1])   # How many
    s = int(cmd[3])-1 # Source crate
    t = int(cmd[5])-1 # Target crate
    batch = state[s][:n][::-1] # Reversed!
    state[s] = state[s][n:]
    state[t] = batch + state[t]

res = ""
for i in range(numcrates):
    res += state[i][0]

print(res)

# Part 2

for i in range(depcrates+2,len(ls)):
    cmd = ls[i].strip().split()
    n = int(cmd[1])   # How many
    s = int(cmd[3])-1 # Source crate
    t = int(cmd[5])-1 # Target crate
    batch = state2[s][:n]
    state2[s] = state2[s][n:]
    state2[t] = batch + state2[t]

res = ""
for i in range(numcrates):
    res += state2[i][0]

print(res)