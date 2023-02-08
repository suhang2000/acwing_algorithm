"""
Binary Exponentiation
"""
"""
875. 快速幂
https://www.acwing.com/problem/content/877/
"""


def binary_exponentiation(a, b, p):
    res = 1 % p  # b==0 and p == 1时，res为 a^0 % 1 = 0
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a = a * a % p
    return res


n = int(input())
for _ in range(n):
    a, b, p = map(int, input().split())
    print(binary_exponentiation(a, b, p))
