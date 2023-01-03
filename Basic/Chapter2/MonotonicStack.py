"""
Monotonic Stack
"""
"""
830. 单调栈
https://www.acwing.com/problem/content/832/
"""

n = int(input())
nums = list(map(int, input().split()))
stack = [-1]
res = []

for x in nums:
    while stack and stack[-1] >= x:
        stack.pop()
    res.append(stack[-1])
    stack.append(x)

print(*res)
