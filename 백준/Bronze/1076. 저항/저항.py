dic = {'black':0, 'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
lst = []
for i in range(2):
    lst.append(dic[input()])
lst.append(10**dic[input()])
# lst[2] = (len(str(lst[2]))-1)*'0'
# if len(str(lst[2])) == 1:
#     lst[2] = 1
# else:
#     lst[2] = (len(str(lst[2]))-1)*'0'

print(int(str(lst[0]) + str(lst[1]))*lst[2])