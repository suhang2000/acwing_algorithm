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

"""
839. 模拟堆
https://www.acwing.com/problem/content/841/
"""


class Heap2:
    def __init__(self):
        self.h = [0]
        self.size = 0
        self.k = 0  # insertion order
        # pointer -> heap, from index (kth inserted) get heap num
        self.ph = [0]
        # heap -> pointer, from heap num get index (kth inserted)
        self.hp = [0]

    def swap(self, x, y):
        # x, y: index in heap
        # x_idx, y_idx: insertion order
        x_idx, y_idx = self.hp[x], self.hp[y]
        self.ph[x_idx], self.ph[y_idx] = y, x
        self.hp[x], self.hp[y] = y_idx, x_idx
        self.h[x], self.h[y] = self.h[y], self.h[x]

    def down(self, x):
        mn_idx = x
        if 2 * x <= self.size and self.h[2 * x] < self.h[mn_idx]:
            mn_idx = 2 * x
        if 2 * x + 1 <= self.size and self.h[2 * x + 1] < self.h[mn_idx]:
            mn_idx = 2 * x + 1
        if x != mn_idx:
            self.swap(x, mn_idx)
            self.down(mn_idx)

    def up(self, x):
        while x // 2 != 0 and self.h[x] < self.h[x // 2]:
            self.swap(x, x // 2)
            x = x // 2

    def insert(self, x):
        self.size += 1
        if len(self.h) == self.size:
            self.h.append(0)
        self.h[self.size] = x
        self.k += 1
        if len(self.hp) == self.size:
            self.hp.append(0)
        self.hp[self.size] = self.k
        self.ph.append(self.size)
        self.up(self.size)

    def pop(self):
        self.swap(1, self.size)
        self.size -= 1
        self.down(1)

    def peek(self):
        return self.h[1]

    def pop_k(self, k):
        x = self.ph[k]
        self.swap(x, self.size)
        self.size -= 1
        self.up(x)
        self.down(x)

    def modify_k(self, k, new_x):
        x = self.ph[k]
        self.h[x] = new_x
        self.up(x)
        self.down(x)


n = int(input())
heap = Heap2()
for _ in range(n):
    line = input().split()
    if line[0] == 'I':
        heap.insert(int(line[1]))
    elif line[0] == 'PM':
        print(heap.peek())
    elif line[0] == 'DM':
        heap.pop()
    elif line[0] == 'D':
        heap.pop_k(int(line[1]))
    else:
        k, x = int(line[1]), int(line[2])
        heap.modify_k(k, x)
