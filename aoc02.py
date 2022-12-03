# Read input

with open("input02.txt") as f:
    ns = f.readlines()

# Part 1

d = {'A':'Rock','B':'Paper','C':'Scissors','X':'Rock','Y':'Paper','Z':'Scissors'}
r = {'Rock':1,'Paper':2,'Scissors':3}

def MyWin(s1,s2):
    if s1=='Rock' and s2=='Paper':
        return(6)
    if s1=='Paper' and s2=='Scissors':
        return(6)    
    if s1=='Scissors' and s2=='Rock':
        return(6)
    if s1==s2:
        return(3)
    return(0)

res = 0

for l in ns:
    p1 = d[l.split()[0]]
    p2 = d[l.split()[1]]
    res += (MyWin(p1,p2) + r[p2])

print(res)

# Part 2

res = 0
ps = ['Rock','Paper','Scissors']

for l in ns:
    p1 = d[l.split()[0]]
    out = l.split()[1]
    if out == 'X': # Need to lose
        i = ps.index(p1)
        p2 = ps[(i-1)%3]
        res += r[p2]
    if out == 'Y': # Need to draw
        p2 = p1
        res += (r[p2]+3)
    if out == 'Z': # Need to win
        i = ps.index(p1)
        p2 = ps[(i+1)%3]
        res += (r[p2]+6)

print(res)        



