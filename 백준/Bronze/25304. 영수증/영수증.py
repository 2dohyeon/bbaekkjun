X = int(input())
N = int(input())
C = 0
for _ in range(N):
    A,B = map(int,input().split())
    C += A*B
if C == X:
    print("Yes")
else:
    print("No")