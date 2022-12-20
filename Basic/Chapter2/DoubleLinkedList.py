"""
Double LinkedList
"""
"""
827. 双链表
https://www.acwing.com/problem/content/829/
"""

e, l, r = [0] * 100010, [0] * 100010, [0] * 100010
idx = 2

# init
r[0] = 1
l[1] = 0


def insert(k, x):
    # 在k的右侧插入x
    global idx
    e[idx] = x
    r[idx] = r[k]
    l[idx] = k
    l[r[k]] = idx
    r[k] = idx
    idx += 1


def remove(k):
    # 删除第k个数
    r[l[k]] = r[k]
    l[r[k]] = l[k]


m = int(input())
for _ in range(m):
    line = input().split()
    if line[0] == 'L':
        insert(0, int(line[1]))
    elif line[0] == 'R':
        insert(l[1], int(line[1]))
    elif line[0] == 'D':
        remove(int(line[1]) + 1)  # 第k个数的下标是 `k + 1` (k-1+2)
    elif line[0] == 'IL':
        insert(l[int(line[1]) + 1], int(line[2]))
    else:
        insert(int(line[1]) + 1, int(line[2]))

i = r[0]
res = []
while i != 1:
    res.append(e[i])
    i = r[i]
print(*res)
