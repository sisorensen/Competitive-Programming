with open("input5.txt") as f:
    l = [line.strip() for line in f]

def part1():
    ranges = [] 
    ids = []
    for s in l:
        if not s:
            continue
        if "-" in s:
            a,b = [int(x) for x in s.split("-")]
            ranges.append((a,b))
        else:
            ids.append(int(s))
    res = 0
    for x in ids:
        for starti,endi in ranges:
            if starti<=x<=endi:
                res += 1
                break
    return res

def part2():
    ranges = [] 
    for s in l:
        if not s:
            continue
        if "-" in s:
            a,b = [int(x) for x in s.split("-")]
            ranges.append((a,b))
    ranges.sort()
    merged = []
    merged.append(list(ranges[0]))
    for i in range(len(ranges)):
        if ranges[i][0]<=merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], ranges[i][1])
        else:
            merged.append(list(ranges[i]))

    res = 0
    for starti,endi in merged:
        res += endi-starti+1
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")