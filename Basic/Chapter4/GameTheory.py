"""
Game Theory
"""
from functools import reduce
from operator import xor

"""
891. Nim游戏
https://www.acwing.com/problem/content/893/
"""

n = int(input())
nums = list(map(int, input().split()))
res = reduce(xor, nums)
print("Yes" if res else "No")

"""
892. 台阶-Nim游戏
https://www.acwing.com/problem/content/894/
"""

n = int(input())
nums = list(map(int, input().split()))
# 只计算奇数台阶异或值
res = reduce(xor, [x for i, x in enumerate(nums) if i % 2 == 0])
print("Yes" if res else "No")

"""
893. 集合-Nim游戏
https://www.acwing.com/problem/content/895/
"""


def sg(x):
    if cache[x] != -1:
        return cache[x]
    state = set()
    for i in s:
        if x >= i:
            state.add(sg(x - i))
    i = 0
    while i in state:
        i += 1
    cache[x] = i
    return i


k = int(input())
s = list(map(int, input().split()))
n = int(input())
h = list(map(int, input().split()))
cache = [-1] * 10010
res = reduce(xor, [sg(x) for x in h])
print("Yes" if res else "No")
