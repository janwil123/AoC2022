# Read input

with open("input15.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

balls = []

for l in ls:
    s = l.split()
    x = int(s[2][2:-1])
    y = int(s[3][2:-1])
    xb = int(s[8][2:-1])
    yb = int(s[9][2:])
    r = abs(x-xb)+abs(y-yb)
    balls.append((x,y,r))

# Part 1

def count(yl):
    pts = []

    for ball in balls:
        if abs(ball[1]-yl) <= ball[2]:
            xa = ball[0] - (ball[2] - abs(ball[1]-yl))
            xl = ball[0] + (ball[2] - abs(ball[1]-yl))
            pts.append((xa,'a'))
            pts.append((xl,'l'))

    pts.sort()

    S = 0
    cnt = 0

    for pt in pts:
        if pt[1] == 'a':
            if cnt == 0: # New segment begins
                xs = pt[0]
                cnt = 1
            else: # cnt > 0
                cnt += 1
        else: # pt[1] == 'l', some segment ends
            cnt -= 1
            if cnt == 0: # All segments end
                S += (pt[0]-xs+1)

    return(S)

print(count(2000000)-1)

# Part 2

def countlim(yl,xmin,xmax):
    pts = []

    for ball in balls:
        if abs(ball[1]-yl) <= ball[2]:
            xa = ball[0] - (ball[2] - abs(ball[1]-yl))
            xl = ball[0] + (ball[2] - abs(ball[1]-yl))
            if xl < xmin:
                continue
            if xa > xmax:
                continue
            if xa < xmin:
                pts.append((xmin,'a'))
            else:
                pts.append((xa,'a'))
            if xl > xmax:
                pts.append((xmax,'l'))
            else:
                pts.append((xl,'l'))

    pts.sort()


    S = 0
    cnt = 0

    for pt in pts:
        if pt[1] == 'a':
            if cnt == 0: # New segment begins
                if pt[0]>0:
                    print(f'x0={pt[0]-1}, y0={yl}')
                xs = pt[0]
                cnt = 1
            else: # cnt > 0
                cnt += 1
        else: # pt[1] == 'l', some segment ends
            cnt -= 1
            if cnt == 0: # All segments end
                S += (pt[0]-xs+1)

    return(S)

M = 4000000

for y in range(M+1):
    n = countlim(y,0,M)

# Output of the above
y0 = 3214126
x0 = 2754143
print(4000000*x0+y0)