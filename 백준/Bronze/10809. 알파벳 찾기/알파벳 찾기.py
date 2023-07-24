#10809번
from string import ascii_lowercase

alph_list = list(ascii_lowercase)
s = list(input())
for i in alph_list:
    if i in s:
        alph_list[alph_list.index(i)] = s.index(i)
    else:
        alph_list[alph_list.index(i)] = -1
print(*alph_list)