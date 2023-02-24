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
