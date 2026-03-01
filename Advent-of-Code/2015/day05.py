with open("input5.txt") as f:
    l = [line.strip() for line in f]

def checks(s):
    se = {"ab", "cd", "pq", "xy"}
    for w in se:
        if w in s:
            return 0
    ok = False
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            ok = True
    if not ok:return 0
    ok = False
    curr = 0
    vow = {"a","e","i","o","u"}
    for c in s:
        if c in vow:
            curr += 1
            if curr == 3:
                return 1
    return 0

def checks2(s):
    ok = False
    for i in range(2,len(s)):
        if s[i] == s[i-2]:
            ok = True
    if not ok:
        return 0
    ok = False
    for i in range(len(s)-3):
        curr = s[i]+s[i+1]
        for j in range(i+2,len(s)-1):
            curr2 = s[j]+s[j+1]
            if curr == curr2:
                ok = True
    return ok

def part1():
    res = 0
    for s in l:
        res += checks(s)
    return res

def part2():
    res = 0
    for s in l:
        res += checks2(s)
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")