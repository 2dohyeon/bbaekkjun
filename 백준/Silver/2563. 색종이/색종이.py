# 100 X 100

count = 0
# 2차원 리스트 선언
paper = [[0 for _ in range(100)] for _ in range(100)]
n = int(input()) # 3
for i in range(n):
    left, bottom = map(int, input().split())
    for y in range(bottom, bottom+10):
        for x in range(left, left+10):
            paper[y][x] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count += 1
print(count) 
