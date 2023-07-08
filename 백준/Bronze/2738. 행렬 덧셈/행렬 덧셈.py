n, m = map(int, input().split(' '))
mat1 = [] # 첫번째 입력 받는 매트릭스
mat2 = [] # 두번째 입력 받는 매트릭스
mat3 = [[0 for j in range(m)] for i in range(n)]
# 입력
for row in range(n):
    col = list(map(int, input().split()))
    mat1.append(col)
for row in range(n):
    col = list(map(int, input().split()))
    mat2.append(col)
# 더하기
for row in range(n):
    for col in range(m):
        mat3[row][col] = mat1[row][col] + mat2[row][col]
# 출력
for row in range(n):
    for col in range(m):
        print(mat3[row][col], end=' ')
    print()