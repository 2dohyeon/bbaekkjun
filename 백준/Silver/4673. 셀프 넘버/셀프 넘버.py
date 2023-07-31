def self_number(n):
    lst = list(str(n))
    lst.append(str(n))
    nlist = sorted(lst, reverse = True)
    num = 0
    for i in range(len(nlist)):
        num += int(nlist[i])
    return num
S_N = []
for i in range(1, 10001):
    S_N.append(self_number(i))

for j in range(1, 10001):
    if j not in S_N:
        print(j)
