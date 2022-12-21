"""
Stack
"""
"""
828. 模拟栈
https://www.acwing.com/problem/content/830/
"""

stack = [0] * 100010
top = -1
m = int(input())

for _ in range(m):
    command = input()
    if command == "pop":
        top -= 1
    elif command == "empty":
        print("NO") if top >= 0 else print("YES")
    elif command == "query":
        print(stack[top])
    else:
        top += 1
        stack[top] = int(command.split()[1])


"""
3302. 表达式求值
https://www.acwing.com/problem/content/3305/
"""

"""
两个栈：
- 数值栈
- 符号栈

优先级：`(` < `+` = `-` < `*` = `/`
优先级判断当前符号是否直接入栈，还是先计算栈内算式
如果当前符号优先级大于栈顶优先级，如栈中为`a+b`，当前为`*`；或者当前为`(`。此时直接入栈
如果当前符号优先级小于等于栈顶，或者是`)`，则先计算栈中算式

**Python中的`//`是向下取整，向0取整可以使用`int()`**
"""

exp = input()
num, op = [], []
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

i = 0


def compute():
    b, a = num.pop(), num.pop()
    o = op.pop()
    res = 0
    if o == '+':
        res = a + b
    elif o == '-':
        res = a - b
    elif o == '*':
        res = a * b
    elif o == '/':
        res = int(a / b)
    num.append(res)


while i < len(exp):
    x = exp[i]
    if x.isdigit():
        # 数字
        j = i + 1
        while j < len(exp) and exp[j].isdigit():
            j += 1
        num.append(int(exp[i:j]))
        i = j - 1
    elif x == '(':
        # 左括号，直接入栈
        op.append(x)
    elif x == ')':
        # 右括号，计算括号内的算式
        while op[-1] != '(':
            compute()
        op.pop()
    else:
        # 运算符
        # 判断当前符号与栈顶符号的优先级，决定是否直接入栈
        while op and priority[op[-1]] >= priority[x]:
            compute()
        op.append(x)
    i += 1

while op:
    compute()
print(num[0])
