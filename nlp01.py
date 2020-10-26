# coding:utf-8

str = 'stressed'

ans = str[::-1]

print(ans)

str2 = u'パタトクカシーー'

ans = str2[::2]

print(ans)

str1 = u'パトカー'
str2 = u'タクシー'
ans = ''.join([i + j for i,j in zip(str1, str2)])

print(ans)


import re
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
splits = str.split()
ans = [len(i) for i in splits]
print(ans)

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
splits = str.split()
one_ch = [1, 5, 6, 7,8, 9, 15, 16, 19]
ans = {}

for i, word in enumerate(splits):
    if i + 1 in one_ch:
        ans[word[:1]] = i + 1
    else:
        ans[word[:2]] = i + 1

print(sorted(ans.items(), key=lambda x:x[1]))


