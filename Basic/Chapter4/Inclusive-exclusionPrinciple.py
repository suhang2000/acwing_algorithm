"""
Inclusive-exclusion Principle
"""
"""
890. 能被整除的数
https://www.acwing.com/problem/content/892/
"""

n, m = map(int, input().split())
prime = list(map(int, input().split()))
res = 0
for i in range(1, 1 << m):
    t, cnt = 1, 0
    for j in range(m):
        if i >> j & 1:
            t *= prime[j]
            if t > n:
                t = -1
                break
            cnt += 1
    if t != -1:
        if cnt % 2:
            res += n // t
        else:
            res -= n // t
print(res)
