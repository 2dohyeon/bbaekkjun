N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
for x in range(M):
    A, B = map(int, input().split())
    nlst = lst[A-1:B]  
    nlst.reverse()
    lst[A-1:B] = nlst
print(*lst)