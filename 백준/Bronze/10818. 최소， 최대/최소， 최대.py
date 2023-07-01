N = int(input())
N_list = list(map(int, input().split()))
max = N_list[0]
min = N_list[0]
for i in range(N):
    if N_list[i] > max:
        max = N_list[i]
    elif N_list[i] < min :
        min = N_list[i]
print(min, max)