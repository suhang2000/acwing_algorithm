"""
Euler Function
"""
"""
873. 欧拉函数
https://www.acwing.com/problem/content/875/
"""


def euler_function(x):
    i = 2
    res = x
    while i <= x // i:
        if x % i == 0:
            res = res - res // i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        res = res - res // x
    return res


n = int(input())
for _ in range(n):
    a = int(input())
    print(euler_function(a))

"""
874. 筛法求欧拉函数
https://www.acwing.com/problem/content/876/
"""

n = int(input())
state = [False] * (n + 1)
prime = []
euler = [0] * (n + 1)
euler[1] = 1  # 1只与本身互质

for i in range(2, n + 1):
    if not state[i]:
        prime.append(i)
        euler[i] = i - 1  # 如果i是质数，则与1~n-1的所有数互质
    for p in prime:
        if p * i > n:
            break
        state[p * i] = True
        if i % p == 0:
            euler[i*p] = p * euler[i]
            break
        euler[i*p] = (p - 1) * euler[i]

print(sum(euler))
