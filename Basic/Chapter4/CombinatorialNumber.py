"""
Combinatorial Number
"""
"""
885. 求组合数 I
https://www.acwing.com/problem/content/887/
递推 O(N^2)
"""


def combinatorial_number1():
    for i in range(N):
        c[i][0] = 1
        for j in range(1, i + 1):
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD


n = int(input())
N = 2010
MOD = 10 ** 9 + 7
c = [[0] * N for _ in range(N)]
combinatorial_number1()
for _ in range(n):
    a, b = map(int, input().split())
    print(c[a][b])

"""
886. 求组合数 II
https://www.acwing.com/problem/content/888/
预处理 O(NlogN)
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

"""
887. 求组合数 III
https://www.acwing.com/problem/content/889/
卢卡斯定理
"""


def lucas(a, b, p):
    if a < p and b < p:
        return C(a, b, p)
    return C(a % p, b % p, p) * lucas(a // p, b // p, p) % p


def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res % p


def C(a, b, p):
    if b > a:
        return 0
    if b > a - b:
        b = a - b
    x, y = 1, 1
    for i in range(b):
        x = x * (a - i) % p
        y = y * (i + 1) % p
    return x * qmi(y, p - 2, p) % p


n = int(input())
for _ in range(n):
    a, b, p = map(int, input().split())
    print(lucas(a, b, p))

"""
888. 求组合数 IV
https://www.acwing.com/problem/content/890/
"""


# 线性筛n以内的质数
def get_primes(n):
    for i in range(2, n + 1):
        if not state[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            state[i * p] = True
            if i % p == 0:
                break


# n的阶乘中，分解质因数p的个数
def get(n, p):
    res = 0
    while n:
        res += n // p
        n //= p
    return res


a, b = map(int, input().split())
primes = []
state = [False] * (a + 1)

get_primes(a)
cnt = len(primes)
prime_cnt = [0] * cnt
for i, p in enumerate(primes):
    prime_cnt[i] = get(a, p) - get(a - b, p) - get(b, p)

res = 1
# 将组合数分解成质因数相乘
for p, c in zip(primes, prime_cnt):
    res *= pow(p, c)
print(res)
