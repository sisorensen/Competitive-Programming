from collections import deque
from z3 import * 

with open("input10.txt") as f:
    inpl = [line.strip() for line in f]

arr = []
buttons = []
jolt = []

for s in inpl:
    curr = s.split()
    arr.append(list(curr[0][1:-1]))
    cl = []
    for x in curr[1:-1]:
        cl.append([int(a) for a in x[1:-1].split(",")])
    buttons.append(cl)
    jolt.append([int(a) for a in curr[-1][1:-1].split(",")])

def part1():
    res = 0
    for i in range(len(arr)):
        curr = ["."]*len(arr[i])
        q = deque()
        vis = {tuple(curr)}
        q.append((curr,0))

        while q:
            cl,steps = q.popleft()
            if cl == arr[i]:
                res += steps
                break
            for but in buttons[i]:
                newl = cl[:]
                if isinstance(but,int):
                    newl[but] = "#" if newl[but] == "." else "."
                else:
                    for ind in but:
                        newl[ind] = "#" if newl[ind] == "." else "."
                if tuple(newl) not in vis:
                    vis.add(tuple(newl))
                    q.append((newl,steps+1))
    return res

def part2():
    res = 0
    for i in range(len(jolt)):
        but = buttons[i]
        t = jolt[i]
        pl = []
        indl = [[] for _ in range(len(t))]
        z = Optimize()

        for j in range(len(but)):
            pl.append(Int(f"p_{j}")) #Z3 integer variable, number of times button j is pressed
            z.add(pl[j]>=0) #For avoiding negative button presses

        for j in range(len(but)):
            for pos in but[j]:
                indl[pos].append(j)

        for k in range(len(indl)):
            currsum = sum([pl[j] for j in indl[k]]) #Sum of button presses that count at pos k
            z.add(currsum == t[k]) #The presses must be equal to target value at pos k to be valid

        z.minimize(sum(pl)) #Minimize total num of presses
        z.check()
        model = z.model()

        curr = 0
        for x in pl:
            curr += model[x].as_long()
        res += curr
    return res

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")