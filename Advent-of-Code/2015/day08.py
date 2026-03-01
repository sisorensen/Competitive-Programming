with open("input8.txt") as f:
    l = [line.strip() for line in f]

def part1():
    resc = 0
    resm = 0
    for s in l:
        resc += len(s)
        i = 0
        while i<len(s):
            if s[i:i+2] == "\\\\":
                i += 2
            elif s[i:i+2] == "\\\"":
                i += 2
            elif s[i:i+2] == "\\x":
                i += 4
            else:
                if s[i] == '"':
                    i += 1
                    continue
                i += 1
            resm += 1
    
    return resc - resm

def part2():
    resc = 0
    resm = 0
    for s in l:
        resc += len(s)
        i = 0
        while i<len(s):
            if s[i] == '"':
                i += 1
                resm += 2
            elif s[i:i+2] == "\\\\":
                i += 2
                resm += 4
            elif s[i:i+2] == "\\\"":
                i += 2
                resm += 4
            elif s[i:i+2] == "\\x":
                i += 4
                resm += 5
            else:
                i += 1
                resm += 1
        resm += 2
    return resm - resc

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")