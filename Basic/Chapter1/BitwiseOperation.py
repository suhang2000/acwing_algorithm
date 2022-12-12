"""
Bitwise Operation
"""
"""
801. 二进制中1的个数
https://www.acwing.com/problem/content/803/
"""

n = int(input())
nums = list(map(int, input().split()))
# method 1
# remove last 1
# x & (x - 1)
for i, x in enumerate(nums):
    cur = 0
    while x:
        x = x & (x-1)
        cur += 1
    nums[i] = cur
print(*nums)
# method 2
# lowbit
# x & -x
for i, x in enumerate(nums):
    cur = 0
    while x:
        x -= x & -x
        cur += 1
    nums[i] = cur
print(*nums)
