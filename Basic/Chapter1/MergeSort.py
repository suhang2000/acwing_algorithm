"""
787. 归并排序
https://www.acwing.com/problem/content/789/

输入样例：
5
3 1 2 4 5
输出样例：
1 2 3 4 5
"""
n = int(input())
nums = list(map(int, input().split()))
tmp = [0] * n
print(n)
print(nums)


def merge(left: int, mid: int, right: int):
    global nums, tmp
    tmp[left: right + 1] = nums[left: right + 1]
    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            nums[k: right + 1] = tmp[j: right + 1]
            break
        elif j > right:
            nums[k: right + 1] = tmp[i: mid + 1]
            break
        elif tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
        else:
            nums[k] = tmp[j]
            j += 1


def merge_sort(left: int, right: int):
    if left >= right: return
    mid = (left + right) >> 1
    merge_sort(left, mid)
    merge_sort(mid + 1, right)
    merge(left, mid, right)


merge_sort(0, n - 1)
print(nums)


"""
Java

import java.io.*;
import java.util.*;

public class Main{
    static int[] tmp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        tmp = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        merge_sort(nums, 0, n - 1);
        for (int x : nums) {
            System.out.print(x);
            System.out.print(" ");
        }
    }
    
    public static void merge_sort(int[] nums, int left, int right) {
        if (left >= right) return;
        int mid = left + ((right - left) >> 1);
        merge_sort(nums, left, mid);
        merge_sort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }
    
    public static void merge(int[] nums, int left, int mid, int right) {
        for(int i = left; i <= right; i++) {
            tmp[i] = nums[i];
        }
        int i = left, j = mid + 1;
        for (int k = left; k <= right; k++) {
            if (i > mid) {
                nums[k] = tmp[j++];
            } else if (j > right) {
                nums[k] = tmp[i++];
            } else if (tmp[i] <= tmp[j]) {
                nums[k] = tmp[i++];
            } else {
                nums[k] = tmp[j++];
            }
        }
    }
}
"""

"""
788. 逆序对的数量
https://www.acwing.com/problem/content/790/

输入样例：
6
2 3 4 5 6 1
输出样例：
5
"""

n = int(input())
nums = list(map(int, input().split()))
tmp = [0] * n
print(n)
print(nums)


def count(left: int, mid: int, right: int) -> int:
    global nums, tmp
    tmp[left: right + 1] = nums[left: right + 1]
    cur = 0
    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            nums[k: right + 1] = tmp[j: right + 1]
            break
        elif j > right:
            nums[k: right + 1] = tmp[i: mid + 1]
            break
        elif tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
        else:
            # tmp[i] > tmp[j]
            cur += mid - i + 1
            nums[k] = tmp[j]
            j += 1
    return cur


def merge_pair(left: int, right: int) -> int:
    if left >= right: return 0
    mid = (left + right) >> 1
    l = merge_pair(left, mid)
    r = merge_pair(mid + 1, right)
    c = count(left, mid, right)
    return l + r + c


print(merge_pair(0, n - 1))
