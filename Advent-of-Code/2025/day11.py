with open("input11.txt") as f:
    l = [line.strip() for line in f]

g = {}
for line in l:
    u,rest = line.split(": ")
    vlist = rest.split()
    g[u] = vlist

def part1():

    def dfs(u):
        if u == "out":
            return 1
        retval = 0
        for v in g[u]:
            retval += dfs(v)
        return retval

    res = dfs("you")
    return res

def part2():
    mem = {}

    def dfs(u,d,f):
        if u == "out":
            return d and f
        retval = 0
        if (u,d,f) in mem:
            return mem[(u,d,f)]
        for v in g[u]:
            if v == "dac":
                newd = 1
            else:
                newd = d
            if v == "fft":
                newf = 1
            else:
                newf = f
            retval += dfs(v,newd,newf)
        mem[(u,d,f)] = retval
        return retval

    res = dfs("svr",0,0)
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")