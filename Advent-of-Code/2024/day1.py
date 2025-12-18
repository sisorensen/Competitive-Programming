with open("input1.txt") as f:
    l = f.readlines()

#Part 1
llist=[]
rlist=[]
for i in range(len(l)):
    a,b=map(int,l[i].split())
    llist.append(a)
    rlist.append(b)
rlist.sort()
llist.sort()

res = 0
for i in range(len(rlist)):
    res += abs(rlist[i]-llist[i])
print(f"Part 1: {res}")

#Part 2
res = 0
countd = {}
for i in range(len(rlist)):
    countd[rlist[i]] = countd.get(rlist[i],0)+1
for num in llist:
    if num in countd:
        res += num*countd[num]
print(f"Part 2: {res}")