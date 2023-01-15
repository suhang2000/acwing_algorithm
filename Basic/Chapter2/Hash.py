"""
Hash
"""
"""
840. 模拟散列表
https://www.acwing.com/problem/content/842/
"""
# 拉链法
N = 100003
h, e, ne = [-1] * N, [0] * N, [0] * N
idx = 0


def insert(x):
    global idx
    k = x % N
    idx += 1
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx


def query(x):
    k = x % N
    i = h[k]
    while i != -1:
        if e[i] == x:
            return True
        i = ne[i]
    return False


n = int(input())
for _ in range(n):
    op, x = input().split()
    x = int(x)
    if op == 'I':
        insert(x)
    else:
        print("Yes" if query(x) else "No")
