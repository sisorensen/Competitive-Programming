from hashlib import md5

with open("input4.txt") as f:
    l = [line.strip() for line in f]
s = l[0]

def findans(n):
    i = 0
    while True:
        curr = s+str(i)
        res = md5(curr.encode()).hexdigest()
        if res[:n] == "0"*n:
            return i
        i += 1

def part1():
    return findans(5)

def part2():
    return findans(6)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")