from collections import deque


def solve(requests, max_requests):
    stack = []
    q = deque()
    for i in range(len(requests)):
        if requests[i] < max_requests[i]:
            stack.append([i, max_requests[i] - requests[i]])
        elif requests[i] > max_requests[i]:
            q.append([i, requests[i] - max_requests[i]])

    ans = 0

    while q and stack:
        a = q[0]
        b = stack[-1]
        if b[1] > a[1]:
            q.popleft()
            stack[-1][1] = b[1] - a[1]
        elif b[1] < a[1]:
            stack.pop()
            q[-1][1] = a[1] - b[1]
        else:
            q.popleft()
            stack.pop()
        ans = max(ans, abs(a[0] - b[0]))

    if q:
        return -1
    return ans


print(solve([4, 1, 3, 2, 4], [4, 2, 1, 5, 3]))
