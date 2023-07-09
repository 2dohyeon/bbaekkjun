# 공넣기
N, M = map(int, input().split())
baguni = []
for x in range(N):
    baguni.append(0)

for y in range(M):
    i, j, k = map(int, input().split())
    for z in range(i-1, j):
        baguni[z] = k
print(*baguni)