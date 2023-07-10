n = int(input())
num_list = []
for i in range(9999999):
    series = str(i)
    if "666" in series:
        num_list.append(i)
    if len(num_list) == n:
        break

print(num_list[n-1])
