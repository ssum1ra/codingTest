import sys
N = int(sys.stdin.readline())

deque = []
for _ in range(N):
    li = list(sys.stdin.readline().split())

    if li[0] == "push_front":
        deque.insert(0, int(li[1]))
    elif li[0] == "push_back":
        deque.append(int(li[1]))
    elif li[0] == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif li[0] == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif li[0] == "size":
        print(len(deque))
    elif li[0] == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif li[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif li[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
