with open("input2.txt") as f:
    l = [line.strip() for line in f]

#Part 1
ranges = l[0].split(",")
res = 0
for i in range(len(ranges)):
    starti,endi = [int(x) for x in ranges[i].split("-")]
    for j in range(starti,endi+1):
        #Number is valid if the first half (as a string) equals the second half
        currs = str(j)
        if len(currs)%2!=0:
            continue
        if currs[:len(currs)//2] == currs[len(currs)//2:]:
            res += j
print(f"Part 1: {res}")

#Part 2
ranges = l[0].split(",")
res = 0
for i in range(len(ranges)):
    starti,endi = [int(x) for x in ranges[i].split("-")]
    for j in range(starti,endi+1):
        currs = str(j)
        #Try every block length k, if the number consists of copies of the prefix it is valid
        valid = False
        for k in range(1,len(currs)//2+1):
            ok = True
            substr = currs[:k]
            for ci in range(k,len(currs),k):
                if currs[ci:ci+k] != substr:
                    ok = False
                    break
            if ok:
                valid = True
                break
        if valid:
            res += j
print(f"Part 2: {res}")