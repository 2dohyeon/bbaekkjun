var = []
for i in range(9):
    var.append(list(map(int, input().split())))

maxvalue = 0
for row in var:
    for element in row:
        if element > maxvalue:
            maxvalue = element

print(maxvalue)


for x in range(9):
    for y in range(9):
        if var[x][y] == maxvalue:
            print(x+1, y+1)