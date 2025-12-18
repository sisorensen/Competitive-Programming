with open("input1.txt") as f:
    l = [line.strip() for line in f]

#Part 1
pos = 50
res = 0
for line in l:
    rot = int(line[1:])
    if line[0]=="L":
        pos = (pos-rot)%100
    else:
        pos = (rot+pos)%100
    if pos == 0:
        res += 1
print(f"Part 1: {res}")

#Part 2
pos = 50
res = 0
for line in l:
    rot = int(line[1:])
    if line[0] == "L":
        if pos == 0:
            pos = 100
        nextpos = pos-rot
        pos = (pos-rot)%100
        if nextpos < 0:
            res += (-(nextpos-99)//100)
    else:
        nextpos = pos+rot
        if (nextpos-1)//100 > 0:
            res += (nextpos-1)//100
        pos = (pos+rot)%100

    if pos == 0:
        res += 1

print(f"Part 2: {res}")