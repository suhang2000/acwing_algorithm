"""
Hash
"""
"""
840. 模拟散列表
https://www.acwing.com/problem/content/842/
"""
# 拉链法 open hashing
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

# 开放寻址法 closed hashing
N = 200003
null = 0x3f3f3f3f
h = [null] * N


def find(x):
    k = x % N
    while h[k] != null and h[k] != x:
        k += 1
        if k == N:
            k = 0
    return k


n = int(input())
for _ in range(n):
    op, x = input().split()
    x = int(x)
    k = find(x)
    if op == 'I':
        h[k] = x
    else:
        print("Yes" if h[k] != null else "No")
