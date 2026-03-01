with open("input15.txt") as f:
    inpl = [line.strip() for line in f]

def part1():
    l = []
    for s in inpl:
        cl = []
        curr = ""
        for c in s:
            if c=="-" or c.isdigit():
                curr += c
            else:
                if curr:
                    cl.append(int(curr))
                curr = ""
        if curr:
            cl.append(int(curr))
        l.append(cl)
    n = 101
    res = 0
    for i in range(n):
        for j in range(n-i):
            for x in range(n-i-j):
                y = 100-i-j-x
                cl = []
                for k in range(4):
                    cl.append(l[0][k]*i + l[1][k]*j + l[2][k]*x + l[3][k]*y)
                curr = 1
                for a in cl:
                    curr *= a if a>0 else 0
                if curr>res:res = curr
    return res

def part2():
    l = []
    for s in inpl:
        cl = []
        curr = ""
        for c in s:
            if c=="-" or c.isdigit():
                curr += c
            else:
                if curr:
                    cl.append(int(curr))
                curr = ""
        if curr:
            cl.append(int(curr))
        l.append(cl)
    n = 101
    res = 0
    for i in range(n):
        for j in range(n-i):
            for x in range(n-i-j):
                y = 100-i-j-x
                cl = []
                for k in range(4):
                    cl.append(l[0][k]*i + l[1][k]*j + l[2][k]*x + l[3][k]*y)
                curr = 1
                for a in cl:
                    curr *= a if a>0 else 0
                check = l[0][4]*i + l[1][4]*j + l[2][4]*x + l[3][4]*y
                if check == 500:
                    if curr>res:res = curr
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")