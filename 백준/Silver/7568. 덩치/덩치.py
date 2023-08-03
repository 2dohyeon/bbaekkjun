# 7568번
N = int(input())
info = [list(map(int,input().split())) for _ in range(N)]
length = len(info)

# print(info)

# [0][0]
# [1][0]
# [2][0]
# ...
# [length-1][0]
# weight = []

# for i in range(length):
#     weight.append(info[i][0])

# height = []
# for j in range(length):
#     height.append(info[j][1])

# print(weight)


# print(height)

# 사람: A 부터 E까지
# 사람보다 몸무게, 키 모두 큰 사람이 몇명인지 센다. 
# + 1 을 해준다.
# print(*)

rank = []
for i in range(1,N+1):
    rank.append(1)

for x in range(N):
    for y in range(N):
    # for i in range(N):
        if info[x][0] < info[y][0] and info[x][1] < info[y][1]: 
      # if human[0] > height and human[1] > weight:
                rank[x] += 1
print(*rank)