with open("input3.txt") as f:
    l = [line.strip() for line in f]

def part1():
    s = l[0]
    vis = {(0,0)}
    cl = [0,0]
    moves = {">":(0,1),"^":(-1,0),"v":(1,0),("<"):(0,-1)}
    for c in s:
        i,j = moves[c]
        cl[0] += i
        cl[1] += j
        vis.add(tuple(cl))
    return len(vis)

def part2():
    s = l[0]
    visl = [{(0,0)},{(0,0)}]
    cl = [[0,0],[0,0]]
    moves = {">":(0,1),"^":(-1,0),"v":(1,0),("<"):(0,-1)}

    for i in range(0,len(s),2):
        x,y = moves[s[i]]
        cl[0][0] += x
        cl[0][1] += y
        visl[0].add(tuple(cl[0]))

        x,y = moves[s[i+1]]
        cl[1][0] += x
        cl[1][1] += y
        visl[0].add(tuple(cl[1]))

    vis = visl[0] | visl[1]
    return len(vis)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")