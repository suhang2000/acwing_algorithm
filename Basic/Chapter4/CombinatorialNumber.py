"""
Combinatorial Number
"""
"""
885. 求组合数 I
https://www.acwing.com/problem/content/887/
"""


def combinatorial_number1():
    for i in range(N):
        c[i][0] = 1
        for j in range(1, i + 1):
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % MOD


n = int(input())
N = 2010
MOD = 10**9+7
c = [[0] * N for _ in range(N)]
combinatorial_number1()
for _ in range(n):
    a, b = map(int, input().split())
    print(c[a][b])

"""
886. 求组合数 II
https://www.acwing.com/problem/content/888/
"""


def qmi(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res % MOD


N = 100010
MOD = 10 ** 9 + 7
# 阶乘和阶乘的逆元
fact = [0] * N
infact = [0] * N
fact[0], infact[0] = 1, 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD
    # 快速幂求逆元： i!的逆元 = (i-1)!的逆元 * i的逆元
    infact[i] = infact[i - 1] * qmi(i, MOD - 2) % MOD

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(fact[a] * infact[b] * infact[a - b] % MOD)
