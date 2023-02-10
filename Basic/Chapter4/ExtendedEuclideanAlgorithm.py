"""
Extended Euclidean Algorithm
"""
"""
https://www.acwing.com/problem/content/879/
"""


def extend_euclidean_algorithm(a, b):
    global x, y
    if b == 0:
        x, y = 1, 0
        return a
    gcd = extend_euclidean_algorithm(b, a % b)
    x, y = y, x - (a // b) * y
    return gcd


n = int(input())
x, y = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    extend_euclidean_algorithm(a, b)
    print(x, y)

"""
878. 线性同余方程
https://www.acwing.com/problem/content/880/
"""

n = int(input())
x, y = 0, 0
for _ in range(n):
    a, b, m = map(int, input().split())
    gcd = extend_euclidean_algorithm(a, m)
    if b % gcd == 0:
        print(x * b // gcd % m)
    else:
        print("impossible")

"""
204. 表达整数的奇怪方式
https://www.acwing.com/problem/content/206/
"""

n = int(input())
x, y = 0, 0
a1, m1 = map(int, input().split())
flag = True
for _ in range(n - 1):
    a2, m2 = map(int, input().split())
    gcd = extend_euclidean_algorithm(a1, -a2)
    if (m2 - m1) % gcd:
        flag = False
        break
    x = x * (m2 - m1) // gcd % abs(a2 // gcd)
    m1 = x * a1 + m1
    a1 = abs(a1 // gcd * a2)
if flag:
    print(m1)
else:
    print(-1)
