# Read input

with open("input08.txt") as f:
    ls = list(map(lambda l:l.strip(), f.readlines()))

m = len(ls)
n = len(ls[0])

# Part 1&2

cnt = 0
maxScore = 0

for i in range(m):
    for j in range(n):
        visibleUp = True
        for k in range(i-1,-1,-1):
            if ls[i][j] <= ls[k][j]:
                visibleUp = False
                upScore = i-k
                break
        if visibleUp:
            upScore = i

        visibleBot = True
        for k in range(i+1,m):
            if ls[i][j] <= ls[k][j]:
                visibleBot = False
                botScore = k-i
                break  
        if visibleBot:
            botScore = n-1-i    

        visibleLeft = True
        for k in range(j-1,-1,-1):
            if ls[i][j] <= ls[i][k]:
                visibleLeft = False
                leftScore = j-k
                break  
        if visibleLeft:
            leftScore = j
            
        visibleRight = True
        for k in range(j+1,n):
            if ls[i][j] <= ls[i][k]:
                visibleRight = False
                rightScore = k-j
                break 
        if visibleRight:
            rightScore = n-1-j
        
        if visibleUp or visibleBot or visibleLeft or visibleRight:
            cnt += 1
        
        score = upScore*botScore*leftScore*rightScore
        if score > maxScore:
            maxScore = score

print(cnt)
print(maxScore)