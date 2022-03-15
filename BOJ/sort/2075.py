#https://www.acmicpc.net/problem/2075
import heapq
N = int(input())
heap = list(map(int,input().split()))
for _ in range(N-1):
    num_list = list(map(int,input().split()))
    for num in num_list:
        if num > heap[0]:
            heapq.heappush(heap,num)
            heapq.heappop(heap)
print(heap[0])
