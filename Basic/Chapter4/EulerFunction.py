"""
Euler Function
"""
"""
873. 欧拉函数
https://www.acwing.com/problem/content/875/
"""


def euler_function(x):
    i = 2
    res = x
    while i <= x // i:
        if x % i == 0:
            res = res - res // i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        res = res - res // x
    return res


n = int(input())
for _ in range(n):
    a = int(input())
    print(euler_function(a))
