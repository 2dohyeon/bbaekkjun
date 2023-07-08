N=int(input())
A = []

for i in range(N):
    A.append(int(input()))
    

for i in range(N):
    for j in range(N-1):
        if A[j] > A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp

for i in range(N):
    print(A[i])