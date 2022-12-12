"""
Discretization
"""
"""
802. 区间和
https://www.acwing.com/problem/content/804/
"""

n, m = map(int, input().split())
add = []
query = []
alls = []
for _ in range(n):
    x, c = map(int, input().split())
    alls.append(x)
    add.append([x, c])
for _ in range(m):
    l, r = map(int, input().split())
    alls.append(l)
    alls.append(r)
    query.append([l, r])
# 去重，排序
alls = sorted(list(set(alls)))
n = len(alls)


# 二分查找，返回x的左边界，然后加1，方便后续前缀和的坐标范围为[1, n]
def get_index(x):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) >> 1
        if alls[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    return l + 1


# 离散化后的数组
nums = [0] * (n + 1)
for i, (x, c) in enumerate(add):
    nums[get_index(x)] += c
presum = [0] * (n + 1)
for i in range(1, n + 1):
    presum[i] = presum[i-1] + nums[i]
for l, r in query:
    print(presum[get_index(r)] - presum[get_index(l) - 1])
