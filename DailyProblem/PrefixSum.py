"""
3956. 截断数组
https://www.acwing.com/problem/content/3959/
"""

n = int(input())
a = list(map(int, input().split()))
pre_sum = [0] * (n + 1)
for i, x in enumerate(a):
    pre_sum[i+1] = pre_sum[i] + x

cnt = res = 0
if pre_sum[-1] % 3 != 0:
    print(0)
else:
    target = pre_sum[-1] // 3
    for j in range(2, n):
        if pre_sum[j-1] == target:
            cnt += 1
        if pre_sum[j] == 2 * target:
            res += cnt
    print(res)
