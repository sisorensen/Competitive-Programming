with open("input3.txt") as f:
    l = [line.strip() for line in f]

#Part 1
res = 0
for num in l:
    maxpair = 0
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            maxpair = max(maxpair,int(num[i] + num[j]))
    res += maxpair
print(f"Part 1: {res}")

#Part 2
batteries = 12
res = 0
for num in l:
    numl = [int(c) for c in num]
    start = 0
    curr = ""
    for _ in range(batteries):
        best = -1
        bestpos = -1
        end = len(numl)-(batteries-len(curr))
        for j in range(start,end+1):
            if numl[j]>best:
                best = numl[j]
                bestpos = j
        curr += str(best)
        start = bestpos+1
    res += int(curr)
print(f"Part 2: {res}")
