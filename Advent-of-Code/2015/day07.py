with open("input7.txt") as f:
    l = [line.strip() for line in f]

def find(cl):
    temp = []
    for c in cl:
        if c in vis:
            temp.append(vis[c])
        elif c.isdigit():
            temp.append(int(c))
    return temp

def part1():
    global vis
    done = [0]*len(l)
    vis = {}
    while True:
        for i in range(len(l)):
            if done[i]:continue
            cl = l[i].split(" -> ")
            curr = cl[0].split()
            if "AND" in curr:
                temp = find([curr[0],curr[2]])
                if len(temp) == 2:
                    vis[cl[1]] = temp[0] & temp[1]
                    done[i] = 1
            elif "OR" in curr:
                temp = find([curr[0],curr[2]])
                if len(temp) == 2:
                    vis[cl[1]] = temp[0] ^ temp[1]
                    done[i] = 1
            elif "LSHIFT" in curr:
                temp = find([curr[0],curr[2]])
                if len(temp) == 2:
                    vis[cl[1]] = temp[0] << temp[1]
                    done[i] = 1
            elif "RSHIFT" in curr:
                temp = find([curr[0],curr[2]])
                if len(temp) == 2:
                    vis[cl[1]] = temp[0] >> temp[1]
                    done[i] = 1
            elif "NOT" in curr:
                temp = find([curr[1]])
                if len(temp) == 1:
                    vis[cl[1]] = ~temp[0]
                    done[i] = 1
            else:
                temp = find([curr[0]])
                if len(temp) == 1:
                    vis[cl[1]] = temp[0]
                    done[i] = 1
                    if cl[1] == "a":
                        return vis["a"]

def part2():
    for i in range(len(l)):
        if i == 89: #My "int -> b" line to be overwritten
            l[i] = f"{part1()} -> b"
    return part1()
    
print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")