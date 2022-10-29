"""
第 75 场周赛
https://www.acwing.com/activity/content/register/2521/
"""

"""
4710. 局部和
"""

n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(d[a - 1:b - 1]))

"""
4711. 排队
"""

n = int(input())
res = [[] for _ in range(4)]
d = {'rat': 0, 'woman': 1, 'child': 1, 'man': 2, 'captain': 3}
for i in range(n):
    name, identity = input().split()
    res[d[identity]].append(name)

for row in res:
    for item in row:
        print(item)

"""
4712. 变换树根
"""

n, r1, r2 = map(int, input().split())
p = list(map(int, input().split()))
p.insert(r1 - 1, 0)


def rever(idx, val):
    if p[idx - 1] == 0:
        p[idx - 1] = val
        return
    rever(p[idx - 1], idx)
    p[idx - 1] = val


rever(p[r2 - 1], r2)
p.pop(r2 - 1)
print(*p)
