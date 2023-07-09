arr = []
for i in range(10):
    arr.append(int(input()))
namuji = []
for i in arr:
    namuji.append(i%42)
A = set(namuji)
print(len(A))  