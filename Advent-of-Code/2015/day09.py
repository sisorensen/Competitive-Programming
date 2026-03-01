with open("input9.txt") as f:
    l = [line.strip() for line in f]

def inpg():
    g = {}
    for s in l:
        cl = s.split()
        if cl[0] not in g:
            g[cl[0]] = []
        if cl[2] not in g:
            g[cl[2]] = []
        g[cl[0]].append((cl[2],int(cl[4])))
        g[cl[2]].append((cl[0],int(cl[4])))
    return g

def part1():
    g = inpg()

    def rec(u,vis):
        if len(vis) == len(g):
            return 0
        retval = float("inf")
        for v,d in g[u]:
            if v not in vis:
                vis.add(v)
                retval = min(retval,d+rec(v,vis))
                vis.remove(v)
        return retval

    res = float("inf")
    for u in g:
        res = min(res,rec(u,{u}))

    return res

def part2():
    g = inpg()

    def rec(u,vis):
        if len(vis) == len(g):
            return 0
        retval = -float("inf")
        for v,d in g[u]:
            if v not in vis:
                vis.add(v)
                retval = max(retval,d+rec(v,vis))
                vis.remove(v)
        return retval

    res = 0
    for u in g:
        res = max(res,rec(u,{u}))

    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")