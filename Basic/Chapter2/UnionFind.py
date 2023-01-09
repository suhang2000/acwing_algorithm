"""
Union Find
"""


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x, y):
        self.p[self.find(x)] = self.find(y)


"""
836. 合并集合
https://www.acwing.com/problem/content/838/
"""

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    c, a, b = input().split()
    a, b = int(a) - 1, int(b) - 1
    if c == 'M':
        uf.merge(a, b)
    else:
        print("Yes" if uf.find(a) == uf.find(b) else "No")
