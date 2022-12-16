"""
Interval Consolidation
"""
"""
803. 区间合并
https://www.acwing.com/problem/content/805/
"""

n = int(input())
seg = []
for _ in range(n):
    l, r = map(int, input().split())
    seg.append((l, r))
seg.sort()
res = 0
st, end = seg[0]
for l, r in seg:
    if l > end:
        res += 1
        st, end = l, r
    else:
        end = max(end, r)
res += 1
print(res)
