"""
785. 快速排序

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
    pivot = nums[left]
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


n = int(input())
nums = list(map(int, input().split()))
# random.shuffle(nums)
quick_sort(nums, 0, n - 1)
print(nums)
