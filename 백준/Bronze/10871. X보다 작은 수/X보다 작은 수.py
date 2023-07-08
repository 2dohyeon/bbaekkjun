N, X = map(int, input().split(' '))
line = list(map(int, input().split(' ')))
for value in line:
    if value < X :
        print(value, end = ' ')