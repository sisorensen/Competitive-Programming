with open("input12.txt") as f:
    l = [line.strip() for line in f]

def part1():
    #Looks difficult, but there are no hard cases - all valid can be filled by a 3x3 tile each
    res = 0
    for i in range(30,len(l)):
        dim,counts = l[i].split(": ")
        r,c = [int(x) for x in dim.split("x")]
        tiles = [int(x) for x in counts.split()]
        if (r//3)*(c//3)>=sum(tiles):
            res += 1
    return res

def part2():
    s = "2025 Advent of Code done"
    return s

print(f"Part 1: {part1()}")
print(part2())