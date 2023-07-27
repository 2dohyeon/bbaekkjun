N = int(input())
star='* '
n_star =' *'
for i in range(1,N+1):
    if i%2==1:
        print(star*N)
    else :
        print(n_star*N)