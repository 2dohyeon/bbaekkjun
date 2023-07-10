N = int(input())

if N % 5 == 0 :
    print(N//5)
else:
    i = 0
    while N % 5 != 0:
        N = N - 3
        i = i + 1

        if N % 5 == 0:
            print(i + (N // 5))
            break
 
        if N == 0:
            print(i)
            break

        if N < 0:
            print(-1)
            break