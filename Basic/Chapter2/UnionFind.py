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


class UnionFind2:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.p[px] = py
        self.size[py] += self.size[px]

    def get_size(self, x):
        return self.size[self.find(x)]


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

"""
837. 连通块中点的数量
https://www.acwing.com/problem/content/839/
"""

n, m = map(int, input().split())
uf = UnionFind2(n + 1)
for _ in range(m):
    line = input().split()
    if line[0] == 'C':
        uf.merge(int(line[1]), int(line[2]))
    elif line[0] == 'Q1':
        print("Yes" if uf.find(int(line[1])) == uf.find(int(line[2])) else "No")
    else:
        print(uf.get_size(int(line[1])))
