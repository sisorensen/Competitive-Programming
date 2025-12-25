with open("input6.txt") as f:
    l = [line.strip() for line in f]

def part1():
    arr = []
    for i in range(len(l)-1):
        nums = [int(x) for x in l[i].split()]
        arr.append(nums)
    ops = l[-1].split()
    res = 0

    for i in range(len(arr[0])):
        curr = int(arr[0][i])
        op = ops[i]               
        for j in range(1,len(arr)):
            val = int(arr[j][i])
            if op == "+":
                curr += val
            else:
                curr *= val
        res += curr
    return res

def part2():
    arr = []
    for i in range(len(l)-1):
        row = [c for c in l[i]]
        arr.append(row)

    ops = l[-1].split()
    res = [1]*len(ops) #Contains the result for each operator (so far) in a list
    ok = False
    ind = 0
    for i in range(len(arr[0])):
        cs = ""              
        for j in range(len(arr)):
            c = arr[j][i]
            if c == " ":
                continue
            cs += str(c)
        if not cs:
            if not ok:
                ind += 1
                ok = True
            continue
        if ok:
            ok = False
        val = int(cs)
        if ops[ind] == "+":
            res[ind] += val
        else:
            res[ind] *= val

    total = 0
    for i in range(len(res)):
        if ops[i] == "+":
            res[i] -= 1
        total += res[i]
    return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")