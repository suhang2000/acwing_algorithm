"""
Kruskal: MST algorithm
O(MlogM)
"""
"""
859. Kruskal算法求最小生成树
https://www.acwing.com/problem/content/861/
"""


class UF:
    def __init__(self, n):
        self.p = list(range(n + 1))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py


n, m = map(int, input().split())
g = []
for _ in range(m):
    u, v, w = map(int, input().split())
    g.append((w, u, v))


def kruskal():
    global n
    g.sort()
    res = cnt = 0
    uf = UF(n)
    for w, u, v in g:
        if uf.find(u) != uf.find(v):
            uf.merge(u, v)
            res += w
            cnt += 1
    return res if cnt == n - 1 else "impossible"


print(kruskal())
