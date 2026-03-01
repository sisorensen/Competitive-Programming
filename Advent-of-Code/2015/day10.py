with open("input10.txt") as f:
    l = [line.strip() for line in f]

def solve(n):
    s = l[0]
    for _ in range(n):
        temp = []
        curr = 1
        ci = s[0]
        for i in range(1,len(s)):                
            if s[i] == ci:
                curr += 1
            else:
                temp.append(str(curr)+ci)
                curr = 1
                ci = s[i]
        temp.append(str(curr)+ci)
        s = "".join(temp)
    return len(s)

print(f"Part 1: {solve(40)}")
print(f"Part 2: {solve(50)}")