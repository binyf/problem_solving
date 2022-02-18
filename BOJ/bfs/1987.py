#https://www.acmicpc.net/problem/1987
from collections import deque
    
def bfs():
    queue = set()
    answer = 1
    queue.add((0, 0, board[0][0]))
    while queue:
        tx, ty, trace = queue.pop()
        for i in range(4):
            nx, ny = tx+dx[i], ty+dy[i]
            if 0 <= ny < R and 0<= nx < C and board[ny][nx] not in trace:
                queue.add((nx, ny, trace + board[ny][nx]))    
            else:
                answer = max(answer,len(trace))                
    return answer
    
R, C = map(int, input().split())
board =  [list(input()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(bfs())