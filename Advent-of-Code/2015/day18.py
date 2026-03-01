with open("input18.txt") as f:
    l = [line.strip() for line in f]

def solve(corners):
    arr = [[c for c in line] for line in l]
    n,m = 100,100
    steps = 100
    moves = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for _ in range(steps):
        change = set()
        for i in range(n):
            for j in range(m):
                if (i,j) in corners:continue
                curr = 0
                for ni,nj in moves:
                    if 0<=i+ni<n and 0<=j+nj<m:
                        if arr[i+ni][j+nj] == "#":
                            curr += 1
                if arr[i][j] == "#" and (curr<2 or curr>3):
                    change.add((i,j))
                if arr[i][j] == "." and curr == 3:
                    change.add((i,j))
        for x,y in change:
            arr[x][y] = "#" if arr[x][y] == "." else "."
    res = 0
    for i in range(n):
        for j in range(m):
            res += 1 if arr[i][j] == "#" else 0
    return res

def part1():
    
    return solve(set())

def part2():
    
    return solve({(0,0),(99,99),(0,99),(99,0)})

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")