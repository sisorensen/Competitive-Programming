with open("input8.txt") as f:
    inpl = [line.strip() for line in f]

def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

def find(x):
    path = []
    while parent[x] != x:
        path.append(x)
        x = parent[x]
    for p in path:
        parent[p] = x
    return x

def union(a,b):
    af,bf = find(a),find(b)
    if af==bf:
        return 0
    if rank[af]<rank[bf]:
        parent[af]=bf
        size[bf] += size[af]
    elif rank[af]>rank[bf]:
        parent[bf]=af
        size[af] += size[bf]
    else:
        parent[bf]=af
        rank[af]+=1
        size[af] += size[bf]
    return 1

#Part 1 - Using Union-find
l = []
for line in inpl:
    l.append([int(x) for x in line.split(",")])

parent = [i for i in range(len(l))]
rank = [0]*len(l)
size = [1]*len(l)
dists = []

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        d = dist(l[i],l[j])
        dists.append((d,i,j))
dists.sort()

for i in range(1000):
    d,ci,cj = dists[i]
    union(ci,cj)

res = []
for i in range(len(l)):
    if parent[i] == i:
        res.append(size[i])
res.sort(reverse=True)
print(f"Part 1: {res[0]*res[1]*res[2]}")

#Part 2
parent = [i for i in range(len(l))]
rank = [0]*len(l)
size = [1]*len(l)

comp = len(l)
for i in range(len(dists)):
    d,ci,cj = dists[i]
    if union(ci,cj):
        comp -= 1
    if comp == 1:break

print(f"Part 2: {l[ci][0]*l[cj][0]}")