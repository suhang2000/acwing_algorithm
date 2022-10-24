"""
785. 快速排序
https://www.acwing.com/activity/content/problem/content/819/

input
5
3 1 2 4 5
output
1 2 3 4 5

"""
import random
from typing import List


def partition(nums: List[int], left: int, right: int) -> int:
    index = random.randint(left, right)
    pivot = nums[index]
    nums[left], nums[index] = nums[index], nums[left]
    # pivot = nums[left]
    i, j = left + 1, right
    while i <= j:
        while i <= right and nums[i] <= pivot:
            i += 1
        while j > left and nums[j] > pivot:
            j -= 1
        if i > j: break
        # swap
        nums[i], nums[j] = nums[j], nums[i]

    nums[left], nums[j] = nums[j], nums[left]
    return j


def quick_sort(nums: List[int], left: int, right: int):
    if left >= right: return
    p = partition(nums, left, right)
    quick_sort(nums, left, p - 1)
    quick_sort(nums, p + 1, right)


# quick sort
n = int(input())
nums = list(map(int, input().split()))
# random.shuffle(nums)
quick_sort(nums, 0, n - 1)
print(nums)

"""
786. 第k个数
https://www.acwing.com/activity/content/problem/content/820/

输入样例：
5 3
2 4 1 5 3
输出样例：
3
"""

# quick select kth number
n, k = map(int, input().split())
nums = list(map(int, input().split()))


def kth_num(nums: List[int], left: int, right: int, k: int):
    p = partition(nums, left, right)
    if p == k:
        return nums[p]
    elif p < k:
        return kth_num(nums, p + 1, right, k)
    else:
        return kth_num(nums, left, p - 1, k)


print(kth_num(nums, 0, n - 1, k - 1))
