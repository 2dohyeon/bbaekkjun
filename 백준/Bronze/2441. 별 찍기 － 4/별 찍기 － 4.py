A = int(input())
for i in range(0, A+1):
    # for x in range(0, i + 1):
    print(i*" "+(A-i)*"*", end='')
    print(end='\n')