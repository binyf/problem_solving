# https://www.acmicpc.net/problem/1022
def strlize(num_list, max_length):
    return [str(num) if len(str(num)) == max_length else ' '*(max_length-len(str(num))) + str(num) for num in num_list]
    
    
positions = list(map(int,input().split()))
lengths = list(map(abs,positions))
L = max(lengths)
N = L*2 + 1
r1, c1, r2, c2 = positions
r1, c1, r2, c2 = r1+L, c1+L, r2+L, c2+L
row = r2 - r1 + 1
col = c2 - c1 + 1
matrix = [[0]*col for _ in range(row)]
directions = [[0,1], [-1,0], [0,-1], [1,0]]
d = 0
if r1 <= L <=r2 and c1 <= L <= c2:
    matrix[L-r1][L-c1] = 1
num = 2
max_count = 1
y = L; x = L
while (True):
    for _ in range(max_count):
        y, x = y + directions[d][0], x + directions[d][1]
        if r1 <= y <= r2 and c1 <= x <= c2:
            matrix[y-r1][x-c1] = num
        num += 1
    if num > N**2:
        break
    d = (d + 1) % 4
    for _ in range(max_count):
        y, x = y + directions[d][0], x + directions[d][1]
        if r1 <= y <=r2 and c1 <= x <= c2:
            matrix[y-r1][x-c1] = num
        num += 1
    if num > N**2:
        break
    d = (d + 1) % 4
    max_count += 1
longest = max(map(max,matrix))
max_length = len(str(longest))
result = [strlize(m,max_length) for m in matrix]
for r in result:
    print(*r)
