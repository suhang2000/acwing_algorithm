"""
Catalan Number
"""
"""
889. 满足条件的01序列
https://www.acwing.com/problem/content/891/
卡特兰数：h(n) = C _a ^b / (n+1)
"""

n = int(input())
MOD = 10 ** 9 + 7
x, y = 1, 1
for i in range(n):
    x = x * (2 * n - i) % MOD
    y = y * (i + 1) % MOD


def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res % p


y = qmi(y, MOD - 2, MOD)
# 除 n+1 也需要变成乘它的逆元
res = x * y * qmi(n + 1, MOD - 2, MOD) % MOD
print(res)
