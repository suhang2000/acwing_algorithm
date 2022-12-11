"""
Dual Pointer
"""
import collections

"""
799. 最长连续不重复子序列
https://www.acwing.com/problem/content/801/
"""

n = int(input())
nums = list(map(int, input().split()))
cnt = collections.Counter()

j = res = 0
for i, x in enumerate(nums):
    cnt[x] += 1
    while cnt[x] > 1:
        cnt[nums[j]] -= 1
        j += 1
    res = max(res, i - j + 1)
print(res)

"""
800. 数组元素的目标和
https://www.acwing.com/problem/content/802/
"""
n, m, x = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 双向对撞指针
i, j = 0, m - 1
for i, a in enumerate(A):
    while a + B[j] > x:
        j -= 1
    if a + B[j] == x:
        print("{} {}".format(i, j))
        break

"""
2816. 判断子序列
https://www.acwing.com/problem/content/2818/
"""

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = j = 0
while i < n and j < m:
    if A[i] == B[j]:
        i += 1
        j += 1
    else:
        j += 1
if i == n:
    print("Yes")
else:
    print("No")
