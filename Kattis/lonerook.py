"""
Lone Rook - one of my favorite problems on Kattis
https://open.kattis.com/problems/lonerook

Task: 
There are one rook and multiple knights on a chessboard. 
The rook has a start square and a target square. The knights are placed on fixed squares.
The rook can move any number of times, but it cannot move to a square that is attacked by a knight.
Is it possible for the rook to get from the start square to the target square? 

Time limit: 11 seconds
My runtime: 0.33 seconds
"""

from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
attack = [[0]*c for _ in range(r)]
knights = [[0]*c for _ in range(r)]
vis = [[0]*c for _ in range(r)]
mk = [(2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2), (-2,1), (-2,-1)] 
q = deque()

# For storing knights and how many knights are attacking each square
def knight(i, j):
    knights[i][j] = 1
    for ni, nj in mk:
        if 0 <= i+ni < r and 0 <= j+nj < c:
            attack[i+ni][j+nj] += 1

for i in range(r):
    s = input().strip()
    for j in range(c):
        if s[j] == "K":
            knight(i, j)
        elif s[j] == "R":
            q.append((i, j))
            vis[i][j] = 1
        elif s[j] == "T":
            goal = (i, j)

# Removes a knight that has been taken. Need to update the attack array, and check if new squares are now free
def knightrem(i,j):
    knights[i][j] = 0
    l = []
    for ni, nj in mk:
        ci, cj = i+ni, j+nj
        if 0 <= ci < r and 0 <= cj < c: 
            attack[ci][cj] -= 1
            if attack[ci][cj] == 0:
                l.append((ci, cj))
    return l

mr = [(1,0), (0,1), (-1,0), (0,-1)] 
possible = False
while q:
    ci, cj = q.popleft()
    if (ci, cj) == goal:
        possible = True
        break

    # Considering each direction for the rook
    for ni, nj in mr:
        i, j = ci, cj
        i += ni
        j += nj
        while True:
            if not (0 <= i < r and 0 <= j < c):
                break
            if vis[i][j] and attack[i][j] == 0:
                break
            vis[i][j] = 1
            if knights[i][j]:
                # Important: if another knight attacks the current knight, they protect each other and can never be taken
                if attack[i][j] == 0:  
                    l = knightrem(i, j)
                    for newi, newj in l:
                        if attack[newi][newj] == 0 and vis[newi][newj]:
                            q.append((newi, newj))
                else:
                    break
            if attack[i][j] == 0:
                q.append((i, j))
            i += ni
            j += nj
print("yes" if possible else "no")