"""
Queue
"""
"""
829. 模拟队列
https://www.acwing.com/problem/content/831/
"""

nums = [0] * 100010
head = tail = 0


def push(x):
    global tail
    nums[tail] = x
    tail += 1


def pop():
    global head
    head += 1
    return nums[head - 1]


def empty():
    global head, tail
    return head == tail


def query():
    global head
    return nums[head]


m = int(input())
for _ in range(m):
    command = input()
    if command == "pop":
        pop()
    elif command == "empty":
        print("YES") if empty() else print("NO")
    elif command == "query":
        print(query())
    else:
        push(int(command.split()[1]))
