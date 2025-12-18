with open("input4.txt") as f:
    l = [line.strip() for line in f]

#Part 1
adj = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
res = 0
row,col = len(l),len(l[0])
for i in range(row):
    for j in range(col):
        curr = 0 
        for ni,nj in adj:
            if 0<=i+ni<row and 0<=j+nj<col:
                if l[i+ni][j+nj] == "@":
                    curr += 1
        if curr<4 and l[i][j] == "@":
            res += 1
print(f"Part 1: {res}")

#Part 2
arr = []
for s in l:
    arr.append([c for c in s])
res = 0
while True:
    done = True
    for i in range(row):
        for j in range(col):
            curr = 0 
            for ni,nj in adj:
                if 0<=i+ni<row and 0<=j+nj<col:
                    if arr[i+ni][j+nj] == "@":
                        curr += 1
            if curr<4 and arr[i][j] == "@":
                res += 1
                done = False
                arr[i][j] = "."
    if done:break
print(f"Part 2: {res}")