with open("input14.txt") as f:
    l = [line.strip() for line in f]

def findt(t,d,fly,rest):
    res = d * fly
    t -= fly
    div = t // (fly+rest)
    res += d * fly * div
    t = t % (fly + rest)
    t -= rest
    res += d * max(0,t)
    return res

def part1():
    t = 2503
    res = 0
    for s in l:
        cl = s.split()
        d,fly,rest = map(int,(cl[3],cl[6],cl[13]))
        res = max(res,findt(t,d,fly,rest))
    return res

def part2():
    cl = []
    curr = []
    for s in l:
        inpl = s.split()
        d,fly,rest = map(int,(inpl[3],inpl[6],inpl[13]))
        cl.append((d,fly,rest))
        curr.append([fly,1])
    n = len(cl)
    t = 2503
    resl = [[0,0] for _ in range(n)]
    for i in range(t):
        for j in range(n):
            curr[j][0] -= 1
            if curr[j][1]:
                resl[j][0] += cl[j][0]
            if curr[j][0] == 0:
                curr[j][1] = not curr[j][1]
                if curr[j][1]:
                    curr[j][0] = cl[j][1]
                else:
                    curr[j][0] = cl[j][2]
        bi,best = [0],resl[0][0]
        for j in range(1,n):
            if resl[j][0]>best:
                bi = [j]
                best = resl[j][0]
            elif resl[j][0] == best:
                bi.append(j)
        for j in bi:
            resl[j][1] += 1
    res = 0
    for i in range(len(resl)):
        res = max(res,resl[i][1])
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
