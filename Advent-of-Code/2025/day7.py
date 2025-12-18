from collections import deque

with open("input7.txt") as f:
    l = [line.strip() for line in f]

#Part 1
vis = [[0]*len(l[0]) for _ in range(len(l))]
res = 0
q = deque()
for i in range(len(l[0])):
    if l[0][i] == "S":
        q.append((0,i))

while q:
    ci,cj = q.popleft()
    if ci == len(l)-1:
        continue
    if l[ci+1][cj] == ".":
        if not vis[ci+1][cj]:
            vis[ci+1][cj] = 1
            q.append((ci+1,cj))
    else:
        res += 1
        if cj-1>=0 and not vis[ci][cj-1]:
            vis[ci][cj-1] = 1
            q.append((ci,cj-1))
        if cj+1<len(l) and not vis[ci][cj+1]:
            vis[ci][cj+1] = 1
            q.append((ci,cj+1))  
print(f"Part 1: {res}")

#Part 2
res = 0
for j in range(len(l[0])):
    if l[0][j] == "S":
        starti,startj = 0,j

def rec(i,j):
    if i == len(l)-1:
        return 1
    if j<0 or j == len(l[0]):
        return 0
    if (i,j) in mem:
        return mem[(i,j)]
    if l[i][j] == ".":
        retval = rec(i+1,j)
    else:
        retval = sum((rec(i,j-1),rec(i,j+1)))
    mem[(i,j)] = retval
    return retval

mem = {}
res = rec(starti,startj)
print(f"Part 2: {res}")