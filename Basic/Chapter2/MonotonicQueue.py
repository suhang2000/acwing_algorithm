"""
Monotonic Queue
"""
import collections
"""
154. 滑动窗口
https://www.acwing.com/problem/content/156/
"""
# 队列里要存下标，不存值。因为要用下标找到首尾方便计算窗口大小
n, k = map(int, input().split())
nums = list(map(int, input().split()))

dq = collections.deque()
res = []
# get minimum
for i, x in enumerate(nums):
    # 1. 计算窗口大小，超过k就移出第一个元素
    if dq and i - dq[0] + 1 > k:
        dq.popleft()
    # 2. 制作单调队列
    while dq and nums[dq[-1]] >= x:
        dq.pop()
    # 3. 添加当前元素
    dq.append(i)
    # 4. 添加结果，打印
    if i >= k - 1:
        res.append(nums[dq[0]])
print(*res)
# get maximum
res.clear()
dq.clear()

for i, x in enumerate(nums):
    if dq and i - dq[0] + 1 > k:
        dq.popleft()
    while dq and nums[dq[-1]] <= x:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        res.append(nums[dq[0]])
print(*res)
