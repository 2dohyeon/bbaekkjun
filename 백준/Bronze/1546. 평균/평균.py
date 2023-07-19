N = int(input())
lst = []
score = list(map(int, input().split()))
for i in score:
    lst.append(i/max(score)*100)

print(sum(lst)/len(lst))