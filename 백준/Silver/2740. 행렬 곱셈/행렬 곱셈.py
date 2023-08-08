
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
# print(A)
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [list(0 for _ in range(K)) for _ in range(N)]

for row_idx in range(N):
    for b_col in range(K):
        for b_row in range(M):
            C[row_idx][b_col] += A[row_idx][b_row] * B[b_row][b_col]  
for element in C:
    print(*element)