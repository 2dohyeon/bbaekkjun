# 공넣기
N, M = map(int, input().split())
baguni = []
for x in range(N):
    baguni.append(x+1)

for y in range(M):
    i, j = map(int, input().split())
    baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
print(*baguni)