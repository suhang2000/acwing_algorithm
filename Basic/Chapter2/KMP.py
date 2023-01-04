"""
KMP
"""
"""
831. KMP字符串
https://www.acwing.com/problem/content/833/
"""

m = int(input())
p = " " + input()  # 下标从1开始
n = int(input())
s = " " + input()  # 下标从1开始

# 1. 构造next数组
ne = [0] * (m + 1)
j = 0
for i in range(2, m + 1):
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j

# 2. 匹配
res = []
j = 0
for i in range(1, n + 1):
    while j and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    if j == m:
        # find
        res.append(i - m)
        j = ne[j]
print(*res)


# Version2: 试一下下标不从1开始怎么写

m = int(input())
p = input()  # 下标从0开始
n = int(input())
s = input()  # 下标从0开始

# 1. 构建next数组
ne = [-1] * m
j = -1
for i in range(1, m):
    while j != -1 and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j
# 2. match
j = -1
res = []
for i in range(n):
    while j != -1 and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    if j == m - 1:
        res.append(i - m + 1)
        j = ne[j]
print(*res)
