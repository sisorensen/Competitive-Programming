with open("input17.txt") as f:
    l = [line.strip() for line in f]
l = [int(x) for x in l]

def part1():
    
    def rec(i,c):
        if c == 0:
            return 1
        if i == len(l):
            return 0
        retval = 0
        if l[i]<=c:
            retval = rec(i+1,c-l[i])
        retval += rec(i+1,c)
        return retval
    res = rec(0,150)

    return res

def part2():
    
    def rec(i,c,k):
        if c == 0:
            return 1 if k == 4 else 0
        if i == len(l):
            return 0
        retval = 0
        if l[i]<=c:
            retval += rec(i+1,c-l[i],k+1)
        retval += rec(i+1,c,k)
        return retval
    res = rec(0,150,0)
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")