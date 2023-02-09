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
