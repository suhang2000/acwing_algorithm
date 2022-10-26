"""
791. 高精度加法
https://www.acwing.com/problem/content/793/

输入样例：
12
23
输出样例：
35
"""
import collections

a = list(input())
b = list(input())
a.reverse()
b.reverse()

if len(a) < len(b):
    a, b = b, a

n, m = len(a), len(b)
res = collections.deque()
carry = 0
for i in range(n):
    cur = int(a[i]) + carry
    if i < m: cur += int(b[i])
    carry = cur // 10
    cur %= 10
    res.appendleft(cur)
if carry:
    res.appendleft(1)

for x in res:
    print(x, end='')
