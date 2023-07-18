from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

max_diff=0
for i in permutations(A,N):
    diff = sum(abs(i[k] -i[k+1]) for k in range(N-1))
    max_diff = max(max_diff, diff)

print(max_diff)