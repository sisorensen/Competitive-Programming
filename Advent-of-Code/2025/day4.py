with open("input4.txt") as f:
    l = [line.strip() for line in f]

def totadj(i,j,l):
    adj = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    row,col = len(l),len(l[0])
    curr = 0
    for ni,nj in adj:
        if 0<=i+ni<row and 0<=j+nj<col:
            if l[i+ni][j+nj] == "@":
                curr += 1
    return curr

def part1():
    res = 0
    row,col = len(l),len(l[0])
    arr = []
    for s in l:
        arr.append([c for c in s])
    for i in range(row):
        for j in range(col):
            curr = totadj(i,j,l) 
            if curr<4 and l[i][j] == "@":
                res += 1
    return res

def part2():
    res = 0
    row,col = len(l),len(l[0])
    arr = []
    for s in l:
        arr.append([c for c in s])
    while True:
        done = True
        for i in range(row):
            for j in range(col):
                curr = totadj(i,j,arr)
                if curr<4 and arr[i][j] == "@":
                    res += 1
                    done = False
                    arr[i][j] = "."
        if done:break
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")