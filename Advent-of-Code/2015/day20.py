with open("input20.txt") as f:
    l = [line.strip() for line in f]
m = int(l[0])

def part1():
    i = 0
    while True:
        curr = 0
        for j in range(1,int(i**0.5)+2):
            if i%j == 0:
                curr += j*10
                curr += (i/j)*10
        if curr>=m:
            return i
        i += 2

def part2():
    i = 0
    while True:
        curr = 0
        for j in range(1,int(i**0.5)+2):
            if i%j == 0:
                if j*50>=i:
                    curr += j*11
                if (i/j)*50>=i:
                    curr += (i/j)*11
        if curr>=m:
            return i
        i += 2

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")