with open("input11.txt") as f:
    l = [line.strip() for line in f]

def checks(s):
    if "i" in s or "o" in s or "u" in s:
        return False
    ok = False
    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1])-1 == ord(s[i+2])-2:
            ok = True
    if not ok:
        return ok
    ok = False 
    for i in range(len(s)-3):
        if s[i] == s[i+1]:
            for j in range(i+2,len(s)-1):
                if s[j] == s[j+1]:
                    ok = True
                    break
        if ok:break
    return ok

def part1():
    s = [c for c in l[0]]
    while True:
        if checks("".join(s)):
            break
        for i in range(len(s)-1,-1,-1):
            if s[i] == "z":
                s[i] = "a"
            else:
                s[i] = chr(ord(s[i])+1)
                break
    return "".join(s)

def part2():
    s = [c for c in l[0]]
    for ind in range(2):
        while True:
            if checks("".join(s)):
                break
            for i in range(len(s)-1,-1,-1):
                if s[i] == "z":
                    s[i] = "a"
                else:
                    s[i] = chr(ord(s[i])+1)
                    break
        if ind == 0:
            for i in range(len(s)-1,-1,-1):
                if s[i] == "z":
                    s[i] = "a"
                else:
                    s[i] = chr(ord(s[i])+1)
                    break
    return "".join(s)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")