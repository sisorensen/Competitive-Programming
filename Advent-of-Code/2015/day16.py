with open("input16.txt") as f:
    l = [line.strip() for line in f]

d = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, 
           "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}

def part1():

    for i in range(len(l)):
        cl = l[i].split()[2:]
        ok = True
        for j in range(0,len(cl),2):
            curr = cl[j+1]
            if curr[-1] == ",":
                curr = curr[:-1]
            if d[cl[j][:-1]] != int(curr):
                ok = False
                break
        if ok:
            return i+1
    
    return 0

def part2():
    greater = {"cats", "trees"}
    lower = {"pomeranians", "goldfish"}
    
    for i in range(len(l)):
        cl = l[i].split()[2:]
        ok = True
        for j in range(0,len(cl),2):
            curr = cl[j+1]
            if curr[-1] == ",":
                curr = curr[:-1]
            s = cl[j][:-1]
            if s in greater:
                if d[cl[j][:-1]] >= int(curr):
                    ok = False
                    break
            elif s in lower:
                if d[cl[j][:-1]] <= int(curr):
                    ok = False
                    break
            else:
                if d[cl[j][:-1]] != int(curr):
                    ok = False
                    break
        if ok:
            return i+1
    return 0

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")