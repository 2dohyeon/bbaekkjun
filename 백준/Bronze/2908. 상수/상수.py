# 2908번
A, B = map(str,input().split())
A = A[::-1]
B = B[::-1]
A = int(A)
B = int(B)
print(max(A,B))