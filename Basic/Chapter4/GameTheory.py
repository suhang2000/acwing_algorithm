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
