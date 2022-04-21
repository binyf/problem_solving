#https://www.acmicpc.net/problem/11000
import heapq

N = int(input())
classes = []
heap = []
for _ in range(N):
    classes.append(list(map(int,input().split())))
classes.sort()

for i in range(N):
    if len(heap) != 0 and heap[0]<= classes[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])

print(len(heap))