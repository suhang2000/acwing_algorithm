"""
Binary Exponentiation
"""
"""
875. 快速幂
https://www.acwing.com/problem/content/877/
"""


def binary_exponentiation(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a = a * a % p
    # 返回时再模一次p，以免特殊情况 b == 0 and p == 1，res = a ^ 0 % 1 = 0
    return res % p


n = int(input())
for _ in range(n):
    a, b, p = map(int, input().split())
    print(binary_exponentiation(a, b, p))

"""
876. 快速幂求逆元
https://www.acwing.com/problem/content/878/
逆元：- 若 a / b % p = a * x % p，则 x 为 b 的逆元，有 b * x % p == 1
     - 根据费马定律 b^(p-1) % p == 1，若p为质数，则逆元 x 为 b^(p-2)。充要条件：b和p互质。
"""

n = int(input())
for _ in range(n):
    a, p = map(int, input().split())
    # 快速幂求 a^(p-2)
    if a % p == 0:
        print("impossible")
    else:
        print(binary_exponentiation(a, p - 2, p))
