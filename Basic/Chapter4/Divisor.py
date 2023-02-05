"""
Divisor
"""
import collections

"""
869. 试除法求约数
https://www.acwing.com/problem/content/871/
"""

n = int(input())
for _ in range(n):
    a = int(input())
    res = []
    i = 1
    while i <= a // i:
        if a % i == 0:
            res.append(i)
            if a // i != i:
                res.append(a // i)
        i += 1
    res.sort()
    print(*res)

# Version 2
n = int(input())
for _ in range(n):
    a = int(input())
    res = []
    i = 1
    while i <= a // i:
        if a % i == 0:
            res.append(i)
        i += 1
    idx = len(res) - 1
    if a // res[-1] == res[-1]:
        idx -= 1
    while idx >= 0:
        res.append(a // res[idx])
        idx -= 1
    print(*res)

"""
870. 约数个数
https://www.acwing.com/problem/content/872/
x = p1^a1 + p2^a2 + ... + pn^an
==> divisor number: (a1+1)*(a2+1)*...(an+1)
"""
# 先分解质因数，统计每个质数及其出现次数，然后利用上述求和公式


def divisor_number(x):
    i = 2
    while i <= x // i:
        while x % i == 0:
            x //= i
            cnt[i] += 1
        i += 1
    if x > 1:
        cnt[x] += 1


MOD = 10 ** 9 + 7
n = int(input())
res = 1
cnt = collections.Counter()
for _ in range(n):
    a = int(input())
    divisor_number(a)
for v in cnt.values():
    res = (res * (v + 1)) % MOD
print(res)

"""
871. 约数之和
https://www.acwing.com/problem/content/873/
x = p1^a1 + p2^a2 + ... + pn^an
==> divisor sum: (p1^0 + p1^1 + ... + p1^a1) * ... * (pn^0 + pn^1 + ... + pn^an)
"""


def prime_divisor(x):
    i = 2
    while i <= x // i:
        while x % i == 0:
            x //= i
            cnt[i] += 1
        i += 1
    if x > 1:
        cnt[x] += 1


MOD = 10 ** 9 + 7
n = int(input())
cnt = collections.Counter()
for _ in range(n):
    a = int(input())
    prime_divisor(a)
res = 1
for p, a in cnt.items():
    t = 1
    for i in range(a):
        t = (t * p + 1) % MOD
    res = (res * t) % MOD
print(res)

"""
872. 最大公约数
https://www.acwing.com/problem/content/874/
辗转相除法
"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))
