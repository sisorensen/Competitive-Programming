with open("input1.txt") as f:
    l = [line.strip() for line in f]
s = l[0]

def part1():
    res = 0
    for c in s:
        res += 1 if c=="(" else -1
    return res

def part2():
    curr = 0
    res = 0
    for c in s:
        curr += 1 if c=="(" else -1
        res += 1
        if curr ==-1:break
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")