"""
Trie
字典树
"""
import collections

"""
835. Trie字符串统计
https://www.acwing.com/problem/content/837/
"""


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.cnt = 0

    def insert(self, arr):
        node = self
        for x in arr:
            node = node.children[x]
        node.cnt += 1

    def search(self, arr):
        node = self
        for x in arr:
            if x not in node.children:
                return 0
            node = node.children[x]
        return node.cnt


n = int(input())
trie = Trie()
for _ in range(n):
    cmd, x = input().split()
    if cmd == 'I':
        trie.insert(x)
    else:
        print(trie.search(x))

# Version 2: 数组模拟

N = 100010
son = [[0] * 26 for _ in range(N)]
cnt = [0] * N
idx = 0


def insert(arr):
    global idx
    p = 0
    for x in arr:
        x = ord(x) - ord('a')
        if son[p][x] == 0:
            idx += 1
            son[p][x] = idx
        p = son[p][x]
    cnt[p] += 1


def search(arr):
    p = 0
    for x in arr:
        x = ord(x) - ord('a')
        if son[p][x] == 0:
            return 0
        p = son[p][x]
    return cnt[p]


n = int(input())
for _ in range(n):
    cmd, x = input().split()
    if cmd == 'I':
        insert(x)
    else:
        print(search(x))

"""
143. 最大异或对
https://www.acwing.com/problem/content/145/
"""


class Trie01:
    def __init__(self):
        self.children = collections.defaultdict(Trie01)

    def insert(self, x):
        node = self
        for i in range(30, -1, -1):
            node = node.children[x >> i & 1]

    def query(self, x):
        node = self
        res = 0
        for i in range(30, -1, -1):
            p = x >> i & 1
            if p ^ 1 in node.children:
                res += 1 << i
                node = node.children[p ^ 1]
            elif p in node.children:
                node = node.children[p]
            else:
                break
        return res


n = int(input())
nums = list(map(int, input().split()))
trie = Trie01()

for x in nums:
    trie.insert(x)

print(max(trie.query(x) for x in nums))

# 手动构造数组模拟

N = 3100010
son = [[0, 0] for _ in range(N)]
idx = 0


def insert(x):
    global idx
    p = 0
    for i in range(30, -1, -1):
        cur = x >> i & 1
        if son[p][cur] == 0:
            idx += 1
            son[p][cur] = idx
        p = son[p][cur]


def search(x):
    p = res = 0
    for i in range(30, -1, -1):
        cur = x >> i & 1
        if son[p][cur ^ 1]:
            res += 1 << i
            p = son[p][cur ^ 1]
        # else:
        #     p = son[p][cur]
        elif son[p][cur]:
            p = son[p][cur]
        else:
            break
    return res


n = int(input())
nums = list(map(int, input().split()))
res = 0
for x in nums:
    insert(x)
    res = max(res, search(x))
print(res)
