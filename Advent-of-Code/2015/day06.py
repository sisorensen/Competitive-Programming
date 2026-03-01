with open("input6.txt") as f:
    l = [line.strip() for line in f]

def part1():
    n = 1000
    arr = [[0]*n for _ in range(n)]
    for s in l:
        cl = s.split()
        endi,endj = [int(x) for x in cl[-1].split(",")]

        if cl[0] == "toggle":
            si,sj = [int(x) for x in cl[1].split(",")]
            for i in range(si,endi+1):
                for j in range(sj,endj+1):
                    arr[i][j] = not arr[i][j]
        else:
            si,sj = [int(x) for x in cl[2].split(",")]
            curr = 1 if cl[1] == "on" else 0
            for i in range(si,endi+1):
                for j in range(sj,endj+1):
                    arr[i][j] = curr
    res = 0
    for i in range(n):
        res += sum(arr[i])

    return res

def part2():
    n = 1000
    arr = [[0]*n for _ in range(n)]
    for s in l:
        cl = s.split()
        endi,endj = [int(x) for x in cl[-1].split(",")]

        if cl[0] == "toggle":
            si,sj = [int(x) for x in cl[1].split(",")]
            for i in range(si,endi+1):
                for j in range(sj,endj+1):
                    arr[i][j] += 2
        else:
            si,sj = [int(x) for x in cl[2].split(",")]
            curr = 1 if cl[1] == "on" else -1
            for i in range(si,endi+1):
                for j in range(sj,endj+1):
                    arr[i][j] = max(curr+arr[i][j],0)
    res = 0
    m = 0
    for i in range(n):
        res += sum(arr[i])
        m = max(m,max(arr[i]))
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")