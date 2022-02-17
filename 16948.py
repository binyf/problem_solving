from collections import deque

def availMove(pos, m):
    temp = [sum(x) for x in zip(pos,m)]
    if temp[0] >= 0 and temp[0] < N and temp[1] >= 0 and temp[1] < N :
        return True, temp
    else:
        return False, -1
    
def bfs():
    queue = deque()
    pos = [r1, c1]
    dest = [r2, c2]
    queue.appendleft((pos, 0))
    while queue:
        temp, lev = queue.pop()
        for m in move:
            avail, nPos = availMove(temp, m)
            if avail:
                if nPos == dest:
                    return lev + 1
                if not cMap[nPos[1]][nPos[0]]:
                    queue.appendleft((nPos, lev + 1))
                    cMap[nPos[1]][nPos[0]] = True
                
    return -1
    
N = int(input())
r1, c1, r2, c2 =  map(int, input().split())
cMap = [[False] * N for _ in range(N)]
move = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
print(bfs())