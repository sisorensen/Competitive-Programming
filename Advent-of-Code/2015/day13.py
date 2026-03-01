from itertools import permutations
with open("input13.txt") as f:
    l = [line.strip() for line in f]

def part1():
    g = {}
    for s in l:
        cl = s.split()
        u,v = cl[0],cl[-1][:-1]
        sign = 1 if cl[2] == "gain" else -1
        if u not in g:
            g[u] = {}
        g[u][v] = int(cl[3])*sign
    cands = list(g.keys())
    res = -float("inf")
    for curr in permutations(cands):
        csum = 0
        for i in range(len(curr)):
            a,b = g[curr[i]][curr[(i-1)%len(curr)]], g[curr[i]][curr[(i+1)%len(curr)]]
            csum += a+b
        if csum>res:
            res = csum
    return res

def part2():
    g = {}
    for s in l:
        cl = s.split()
        u,v = cl[0],cl[-1][:-1]
        sign = 1 if cl[2] == "gain" else -1
        if u not in g:
            g[u] = {}
        g[u][v] = int(cl[3])*sign

    g["Me"] = {}
    for k in g.keys():
        g["Me"][k] = 0
        g[k]["Me"] = 0

    cands = list(g.keys())
    res = -float("inf")
    for curr in permutations(cands):
        csum = 0
        for i in range(len(curr)):
            a,b = g[curr[i]][curr[(i-1)%len(curr)]], g[curr[i]][curr[(i+1)%len(curr)]]
            csum += a+b
        if csum>res:
            res = csum
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")