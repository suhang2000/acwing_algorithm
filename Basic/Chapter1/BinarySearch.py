"""
789. 数的范围
https://www.acwing.com/problem/content/791/

输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
"""

n, q = map(int, input().split())
nums = list(map(int, input().split()))
query = [0] * q
for i in range(q):
    query[i] = int(input())


def binary_search(target: int) -> int:
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bound(idx):
    target = nums[idx]
    # left bound
    left, right = 0, idx - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    a = left
    # right bound
    left, right = idx + 1, n - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    b = right
    return a, b


for q in query:
    idx = binary_search(q)
    if idx == -1:
        print('-1 -1')
    else:
        print(*bound(idx))

"""
790. 数的三次方根
https://www.acwing.com/problem/content/792/

输入样例：
1000.00
输出样例：
10.000000
"""

n = float(input())
# left, right = (0, n) if n >= 0 else (n, 0)
left, right = -10000, 10000
mid = n
while right - left >= 1e-8:
    mid = (left + right) / 2
    if mid * mid * mid < n:
        left = mid
    else:
        right = mid
print("{:.6f}".format(mid))
