"""
Combinatorial Number
"""
"""
885. 求组合数 I
https://www.acwing.com/problem/content/887/
"""


def combinatorial_number1():
    for i in range(N):
        c[i][0] = 1
        for j in range(1, i + 1):
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % MOD


n = int(input())
N = 2010
MOD = 10**9+7
c = [[0] * N for _ in range(N)]
combinatorial_number1()
for _ in range(n):
    a, b = map(int, input().split())
    print(c[a][b])
