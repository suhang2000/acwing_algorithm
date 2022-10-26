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

"""
792. 高精度减法
https://www.acwing.com/problem/content/794/

输入样例：
32
11
输出样例：
21
"""

a = [int(x) for x in list(input())]
b = [int(x) for x in list(input())]


# whether a >= b
def cmp(a, b):
    if len(a) != len(b): return len(a) > len(b)
    for x, y in zip(a, b):
        if x < y:
            return False
        elif x > y:
            return True
    return True


# 1. 判断大小，正负
minus = False
if not cmp(a, b):
    # a < b
    a, b = b, a
    minus = True

a.reverse()
b.reverse()

# 2. 逐位相减
res = collections.deque()
carry = 0
n, m = len(a), len(b)
for i in range(n):
    cur = a[i] - carry
    if i < m:
        cur -= b[i]
    if cur < 0:
        cur += 10
        carry = 1
    else:
        carry = 0
    res.appendleft(cur)

# 3. 移出前导0
while len(res) > 1 and res[0] == 0:
    res.popleft()

if minus:
    print("-", end='')
for x in res:
    print(x, end='')
