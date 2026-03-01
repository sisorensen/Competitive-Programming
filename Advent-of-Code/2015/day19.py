with open("input19.txt") as f:
    l = [line.strip() for line in f]

def part1():
    d = {}
    for s in l[:-2]:
        cl = s.split()
        if cl[0] not in d:
            d[cl[0]] = []
        d[cl[0]].append(cl[2])
    s = l[-1]
    vis = set()
    for i in range(len(s)):
        if s[i] in d:
            for cs in d[s[i]]:
                vis.add(s[:i]+cs+s[i+1:])
        ns = s[i:i+2]
        if ns in d:
            for cs in d[ns]:
                vis.add(s[:i]+cs+s[i+2:])
    return len(vis)

def part2():

    d = {}
    lengths = set()
    for s in l[:-2]:
        cl = s.split()
        lengths.add(len(cl[2]))
        d[cl[2]] = cl[0]    
    lengths = list(lengths)
    vis = {l[-1]}

    def rec(s,step):
        if s == "e":
            print(f"Part 2: {step}")
            exit()

        for i in range(len(s)-1,-1,-1):
            for klen in lengths:
                if s[i:i+klen] in d:
                    curr = s[:i] + d[s[i:i+klen]] + s[i+klen:]
                    if curr not in vis:
                        vis.add(curr)
                        rec(curr,step+1)
    rec(l[-1],0)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")