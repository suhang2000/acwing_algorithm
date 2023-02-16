"""
Gauss Elimination
"""
"""
883. 高斯消元解线性方程组
https://www.acwing.com/problem/content/885/
"""


def gauss():
    row = 0
    for col in range(n):
        t = row
        # 找到绝对值最大的行
        for i in range(row, n):
            if abs(a[i][col]) > abs(a[t][col]):
                t = i
        if abs(a[t][col]) < EPS:
            continue
        # 将绝对值最大的行换到顶行(当前行row)
        a[row], a[t] = a[t], a[row]
        # 将当前行的首位系数变为1
        for i in range(n, col - 1, -1):
            a[row][i] /= a[row][col]
        # 用当前行消掉下面所有列
        for i in range(row + 1, n):
            if abs(a[i][col]) > EPS:
                for j in range(n, col - 1, -1):
                    a[i][j] -= a[row][j] * a[i][col]
        row += 1

    if row < n:
        for i in range(row, n):
            if abs(a[i][n]) > EPS:
                return 2  # no solution
        return 1  # infinite solutions
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            a[i][n] -= a[i][j] * a[j][n]
    return 0


EPS = 1e-8
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(float, input().split())))

# gauss elimination
res = gauss()
if res == 2:
    print("No solution")
elif res == 1:
    print("Infinite group solutions")
else:
    for i in range(n):
        if abs(a[i][n]) < EPS:
            a[i][n] = 0
        print("{:.2f}".format(a[i][n]))
