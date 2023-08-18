# 덩치
N = int(input())

rank = []
for i in range(N):
    rank.append(1)
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

for x in range(N):
    for y in range(N):
        if lst[x][0] > lst[y][0] and lst[x][1] > lst[y][1]:
            rank[y] += 1
print(*rank)