import sys
x, y = map(int,input().split())
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
n = 0
for i in range(x) :   
    n += date[i]
n1 = n + y
print(yoil[n1%7])