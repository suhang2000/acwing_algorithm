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

"""
867. 分解质因数
https://www.acwing.com/problem/content/869/
"""


def decomposition_prime_factors(x):
    i = 2
    while i <= x // i:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                x //= i
                cnt += 1
            print(i, cnt, sep=' ')
        i += 1
    if x > 1:
        print(x, 1, sep=' ')
    print()


n = int(input())
for _ in range(n):
    a = int(input())
    decomposition_prime_factors(a)

"""
868. 筛质数
https://www.acwing.com/problem/content/870/
"""

"""埃氏筛法"""
n = int(input())
prime = []
state = [False] * (n + 1)
for i in range(2, n + 1):
    if not state[i]:
        prime.append(i)
        j = 2
        while i * j <= n:
            state[i * j] = True
            j += 1
print(len(prime))
