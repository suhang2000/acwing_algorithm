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

