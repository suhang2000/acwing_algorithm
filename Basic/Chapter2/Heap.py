"""
Heap
"""
"""
838. 堆排序
https://www.acwing.com/problem/content/840/
"""


# min heap
class Heap:
    def __init__(self, n, nums):
        # 下标从1开始
        self.h = [0] + nums
        self.size = n
        # build, from bottom to top
        # size // 2, first not leaf node
        for x in range(n // 2, 0, -1):
            self.down(x)

    def down(self, x):
        min_idx = x
        if 2 * x <= self.size and self.h[2 * x] < self.h[min_idx]:
            min_idx = 2 * x
        if 2 * x + 1 <= self.size and self.h[2 * x + 1] < self.h[min_idx]:
            min_idx = 2 * x + 1
        if min_idx != x:
            self.h[x], self.h[min_idx] = self.h[min_idx], self.h[x]
            self.down(min_idx)

    def up(self, x):
        while x // 2 != 0 and self.h[x] < self.h[x // 2]:
            self.h[x], self.h[x // 2] = self.h[x // 2], self.h[x]
            x //= 2

    def top(self):
        return self.h[1]

    def pop(self):
        t = self.h[1]
        self.h[1] = self.h[self.size]
        self.size -= 1
        self.down(1)
        return t


n, m = map(int, input().split())
nums = list(map(int, input().split()))
heap = Heap(n, nums)
res = [0] * m
for i in range(m):
    res[i] = heap.pop()
print(*res)
