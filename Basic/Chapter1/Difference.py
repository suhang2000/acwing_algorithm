"""
Difference
"""
"""
797. 差分
https://www.acwing.com/problem/content/799/
"""


def difference(l, r, c):
    diff[l] += c
    if r + 1 < n:
        diff[r + 1] -= c


n, m = map(int, input().split())
arr = list(map(int, input().split()))
diff = [0] * n
# construct 1
# diff[0] = arr[0]
# for i in range(1, n):
#     diff[i] = arr[i] - arr[i-1]
# construct 2
for i in range(n):
    difference(i, i, arr[i])

# difference
for _ in range(m):
    l, r, c = map(int, input().split())
    difference(l - 1, r - 1, c)

# print result
for i in range(1, n):
    diff[i] += diff[i - 1]
print(*diff)

"""
798. 差分矩阵
https://www.acwing.com/problem/content/800/
"""
n, m, q = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
diff = [[0] * (m + 2) for _ in range(n + 2)]


def diff_2dim(x1, y1, x2, y2, c):
    diff[x1][y1] += c
    diff[x2 + 1][y1] -= c
    diff[x1][y2 + 1] -= c
    diff[x2 + 1][y2 + 1] += c


# construct
for i in range(1, n+1):
    for j in range(1, m+1):
        diff_2dim(i, j, i, j, matrix[i-1][j-1])

# difference
for _ in range(q):
    x1, y1, x2, y2, c = map(int, input().split())
    diff_2dim(x1, y1, x2, y2, c)

for i in range(1, n+1):
    for j in range(1, m+1):
        diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
    print(*diff[i][1:-1])
