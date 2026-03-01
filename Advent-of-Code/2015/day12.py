import json

with open("input12.txt") as f:
    inp = json.load(f)

def part1():

    def rec(obj):
        if isinstance(obj, int):
            return obj        
        
        if isinstance(obj, list):
            return sum([rec(v) for v in obj])
        
        if isinstance(obj, dict):
            return sum([rec(v) for v in obj.values()])
        
        return 0
        
    return rec(inp)

def part2():
    
    def rec(obj):
        if isinstance(obj, int):
            return obj        
        
        if isinstance(obj, list):
            return sum([rec(v) for v in obj if v!="red"])
        
        if isinstance(obj, dict):
            l = [rec(v) for v in obj.values()]
            if "red" in l:
                return 0
            return sum(l)
        
        if obj == "red":
            return "red"
        
        return 0
    
    return rec(inp)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")