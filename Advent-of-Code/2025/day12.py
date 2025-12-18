with open("input12.txt") as f:
    l = [line.strip() for line in f]

#Part 1
#Trick: comes off as a hard problem, but there are no hard cases - all valid can be filled by a 3x3 tile each
res = 0
for i in range(30,len(l)):
    dim,counts = l[i].split(": ")
    r,c = [int(x) for x in dim.split("x")]
    tiles = [int(x) for x in counts.split()]
    if (r//3)*(c//3)>=sum(tiles):
        res += 1
print(f"Part 1: {res}")
print("2025 Advent of Code done")