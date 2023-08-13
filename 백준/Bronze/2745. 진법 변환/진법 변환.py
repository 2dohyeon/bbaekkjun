import sys
lst = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

N, B = sys.stdin.readline().split()
B = int(B)
sum = 0
for i in range(len(N)):
    N_r = list(reversed(N))
    A = (B**i)*lst.index(N_r[i])
    sum += A

print(sum)