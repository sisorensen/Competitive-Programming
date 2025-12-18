from collections import deque

with open("input9.txt") as f:
    l = [line.strip() for line in f]

points = []
for s in l:
    points.append([int(x) for x in s.split(",")])

#Part 1
res = 0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        a,b = points[i]
        c,d = points[j]
        curr = ((max(a,c)-min(a,c))+1)*((max(b,d)-min(b,d))+1) 
        if curr>res:
            res = curr
print(f"Part 1: {res}")

#Part 2
#Instead of having true coords, sort them and only keep track of coord indices (compression)
#Then, I can do the BFS approach - much smaller dims compared to with full coordinates

xset,yset = set(),set()
for a,b in points:
    xset.add(a)
    yset.add(b)
xl = sorted(list(xset))
yl = sorted(list(yset))
n = len(xl)+2

arr = [["."]*n for _ in range(n)]
xd,yd = {},{}
for i in range(len(xl)):
    xd[yl[i]] = i+1
    yd[xl[i]] = i+1
bl = [[1]*n for _ in range(n)] #Initially, all coords is inside. Then do bfs to remove all outside

for i in range(len(points)):
    b,a = points[i]
    a,b = xd[a],yd[b]

    d,c = points[(i+1)%len(l)]
    c,d = xd[c],yd[d]
    if a==c:
        for j in range(min(b,d),max(b,d)+1):
            arr[a][j] = "#"
    else:
        for j in range(min(a,c),max(a,c)+1):
            arr[j][b] = "#"

#Now: fill outside with 0s
q = deque()
q.append((0,0))
bl[0][0] = 0
moves = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    i,j = q.popleft()
    for ni,nj in moves:
        if 0<=i+ni<n and 0<=j+nj<n:
            if arr[i+ni][j+nj] == ".":
                if bl[i+ni][j+nj]:
                    bl[i+ni][j+nj] = 0
                    q.append((i+ni,j+nj))

res = 0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        b,a = points[i]
        d,c = points[j]
        curr = ((max(a,c)-min(a,c))+1)*((max(b,d)-min(b,d))+1) 
        a,b = xd[a],yd[b]
        c,d = xd[c],yd[d]
        if curr<=res:
            continue
        #Check if all coords on the rectangle frame is inside (thats good enough)
        ok = True
        for x in range(min(a,c),max(a,c)+1):
            if not bl[x][b] or not bl[x][d]:
                ok = False
                break
        if not ok:
            continue
        for x in range(min(b,d),max(b,d)+1):
            if not bl[a][x] or not bl[c][x]:
                ok = False
                break
        if ok:
            res = curr
print(f"Part 2: {res}")