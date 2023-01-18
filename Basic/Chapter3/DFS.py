"""
DFS
"""
"""
842. 排列数字
https://www.acwing.com/problem/content/844/
"""
# version 1 状态数组
n = int(input())
path = [0] * n
used = [False] * (n + 1)


def dfs(idx):
    global n
    if idx == n:
        print(*path)
        return
    for i in range(1, n + 1):
        if not used[i]:
            path[idx] = i
            used[i] = True
            dfs(idx + 1)
            used[i] = False


dfs(0)

# version 2 状态压缩
n = int(input())
path = [0] * n


def dfs(idx, state):
    global n
    if idx == n:
        print(*path)
        return
    for i in range(1, n + 1):
        if state >> i & 1 == 0:
            path[idx] = i
            dfs(idx + 1, state + (1 << i))


dfs(0, 0)


"""
n-皇后问题
https://www.acwing.com/problem/content/845/
"""
# version 1 按行搜 + 状态压缩
n = int(input())
g = [['.'] * n for _ in range(n)]


def dfs(row, col_state, dig_state, anti_dig_state):
    global n
    if n == row:
        for r in g:
            for item in r:
                print(item, end='')
            print()
        print()
        return
    # enumerate column
    for col in range(n):
        # diagonal: y=x+b ==> b=y-x ==> maybe negative, so b = (y - x) + n, or b = (y - x) % 2n
        # range: -(n-1) ~ n-1 ==> 1 ~ 2n-1
        # anti-diagonal: y = -x + b ==> b = y + x
        # range: 0 ~ 2(n-1)
        # code 1
        # mod = 2 * n
        # if col_state >> col & 1 == 0 and dig_state >> ((col - row) % mod) & 1 == 0 and anti_dig_state >> (col + row) & 1 == 0:
        #     g[row][col] = 'Q'
        #     dfs(row + 1, col_state | (1 << col), dig_state | (1 << ((col - row) % mod)), anti_dig_state | (1 << (col + row)))
        #     g[row][col] = '.'
        # another code
        if col_state >> col & 1 == 0 and dig_state >> (col - row + n) & 1 == 0 and anti_dig_state >> (col + row) & 1 == 0:
            g[row][col] = 'Q'
            dfs(row + 1, col_state | (1 << col), dig_state | (1 << (col - row + n)), anti_dig_state | (1 << (col + row)))
            g[row][col] = '.'


dfs(0, 0, 0, 0)


# version 2 按格搜
n = int(input())
g = [['.'] * n for _ in range(n)]


def dfs(row, col, queen, row_state, col_state, dig_state, anti_dig_state):
    global n
    if queen == n:
        for r in g:
            for item in r:
                print(item, end='')
            print()
        print()
        return
    if col == n:
        row += 1
        col = 0
    if row == n:
        return
    # select
    if row_state >> row & 1 == 0 and col_state >> col & 1 == 0 and \
            dig_state >> (col - row + n) & 1 == 0 and anti_dig_state >> (col + row) & 1 == 0:
        g[row][col] = 'Q'
        dfs(row, col + 1, queen + 1, row_state | (1 << row), col_state | (1 << col), dig_state | (1 << (col - row + n)),
            anti_dig_state | (1 << (col + row)))
        g[row][col] = '.'
    # not select
    dfs(row, col + 1, queen, row_state, col_state, dig_state, anti_dig_state)


dfs(0, 0, 0, 0, 0, 0, 0)
