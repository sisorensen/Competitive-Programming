with open("input2.txt") as f:
    l = [line.strip() for line in f]

def part1():
    res = 0
    for s in l:
        cl = [int(x) for x in s.split("x")]
        curr = 0
        for i in range(len(cl)-1):
            for j in range(i+1,len(cl)):
                curr += cl[i]*cl[j]*2
        cl.sort()
        curr += cl[0]*cl[1]
        res += curr
    return res

def part2():
    res = 0
    for s in l:
        cl = [int(x) for x in s.split("x")]
        cl.sort()
        curr = cl[0]*2+cl[1]*2+cl[0]*cl[1]*cl[2]
        res += curr
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")