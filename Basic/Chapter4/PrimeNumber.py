"""
Prime number
"""
"""
866. 试除法判定质数
https://www.acwing.com/problem/content/868/
"""

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 1:
        print("No")
        continue
    i = 2
    flag = True
    while i <= a // i:
        if a % i == 0:
            flag = False
            break
        i += 1
    print("Yes" if flag else "No")
