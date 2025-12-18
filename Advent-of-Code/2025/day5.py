with open("input5.txt") as f:
    l = [line.strip() for line in f]

ranges = [] 
ids = []
for s in l:
    if not s:
        continue
    if "-" in s:
        a,b = [int(x) for x in s.split("-")]
        ranges.append((a,b))
    else:
        ids.append(int(s))
res = 0
for x in ids:
    for starti,endi in ranges:
        if starti<=x<=endi:
            res += 1
            break
print(f"Part 1: {res}")

#Part 2
ranges.sort()
merged = []
done = [0]*len(ranges)

for i in range(len(ranges)):
    if done[i]:
        continue
    done[i] = 1
    curr = [ranges[i][0],ranges[i][1]]
    #Merge all intervals that overlap with current one
    while True:
        ok = True
        for j in range(i+1,len(ranges)):
            if done[j]:
                continue
            starti,endi = ranges[j]
            if starti<=curr[1]:
                if endi>curr[1]:
                    curr[1] = endi
                    ok = False
                done[j] = 1
        if ok:
            break
    merged.append(curr)

res = 0
for starti,endi in merged:
    res += endi-starti+1
print(f"Part 2: {res}")
