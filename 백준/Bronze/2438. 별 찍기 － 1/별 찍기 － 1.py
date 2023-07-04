A = int(input())
for y in range(0, A):
    for x in range(0, y + 1):
        print("*", end='')
    print(end='\n')