N = list(input())

lst = []
for i in range(len(N)):
    first_gop = 1
    second_gop = 1
    if len(N) == 1:
        break
    first = N[:i+1]
    second = N[i+1:len(N)+1]
    for j in range(len(first)):
        first_gop *= int(first[j])
    for k in range(len(second)):
        second_gop *= int(second[k])
    if first_gop == second_gop:
        lst.append("YES")
    else:
        lst.append("NO")

if "YES" in lst:
    print("YES")
else:
    print("NO")