import sys
lst = []
N = int(input())
for i in range(N):
    A = sys.stdin.readline()
    if 'push' in A:
        X, Y = A.split()
        Y = int(Y)
        lst.append(Y)
    elif 'top' in A:
        if lst :
            print(lst[-1])
        else :
            print(-1)
    elif 'size' in A:
        print(len(lst))
    elif 'empty' in A:
        if len(lst) ==0:
            print(1)
        else:
            print(0)
    elif 'pop' in A:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

            
