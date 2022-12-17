"""
Single LinkedList
"""
"""
826. 单链表
https://www.acwing.com/problem/content/828/
"""

head, idx = -1, 0
e, ne = [0] * 100010, [0] * 100010


def insert_head(x):
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


def delete_k(k):
    global idx, head
    if k == 0:
        # delete head
        head = ne[head]
    else:
        # kth number -> idx = k - 1
        ne[k-1] = ne[ne[k-1]]


def insert_k(k, x):
    global idx, head
    # kth number -> idx = k - 1
    e[idx] = x
    ne[idx] = ne[k-1]
    ne[k-1] = idx
    idx += 1


m = int(input())
for _ in range(m):
    line = input().split()
    if line[0] == 'H':
        insert_head(int(line[1]))
    elif line[0] == 'D':
        delete_k(int(line[1]))
    else:
        insert_k(int(line[1]), int(line[2]))

i = head
res = []
while i != -1:
    res.append(e[i])
    i = ne[i]
print(*res)
