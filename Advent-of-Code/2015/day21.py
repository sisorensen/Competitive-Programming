with open("input21.txt") as f:
    l = [line.strip() for line in f]

def battle(hp,damage,armor,bhp,bdamage,barmor):
    while True:
        bhp -= max(damage-barmor,1)
        if bhp<=0:
            return True
        hp -= max(bdamage-armor,1)
        if hp<=0:
            return False

def getcombs():
    pl = []
    weapon = [(8,4),(10,5),(25,6),(40,7),(74,8)]
    armor = [(13,1),(31,2),(53,3),(75,4),(102,5),(0,0)]
    rings = [(25,1),(50,2),(100,3),(20,1),(40,2),(80,3),(0,0)]
    
    for i in range(5):
        for j in range(6):
            for x in range(6):
                for y in range(x,6):
                    cost, hp, dmg, arm = 0,100,0,0
                    dmg += weapon[i][1]
                    cost += weapon[i][0]
                    cost += armor[j][0]
                    arm += armor[j][1]                        
                    cost += rings[x][0]
                    if x<3:
                        dmg += rings[x][1]
                    else:
                        arm += rings[x][1]
                    if y != x:
                        cost += rings[y][0]
                        if y<3:
                            dmg += rings[y][1]
                        else:
                            arm += rings[y][1]
                    pl.append([cost,hp,dmg,arm])
    pl.sort()
    return pl

def part1():
    boss = [] #hp, damage, armor
    for s in l:
        cl = s.split()
        boss.append(int(cl[-1]))
    pl = getcombs()

    for i in range(len(pl)):
        cost, hp, damage,armor = pl[i]
        if battle(hp,damage,armor,boss[0],boss[1],boss[2]):
            return cost
        
    return pl[-1][0]


def part2():
    boss = [] #hp, damage, armor
    for s in l:
        cl = s.split()
        boss.append(int(cl[-1]))
    pl = getcombs()

    for i in range(len(pl)-1,-1,-1):
        cost, hp, damage, armor = pl[i]
        if not battle(hp,damage,armor,boss[0],boss[1],boss[2]):
            return cost

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")