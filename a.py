def solve(arr=[10, -7, -10, 33]):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    arr.sort()
    print(arr)

    def binarySearch(x, j):
        ans = j
        l, r = 0, j
        while l <= r:
            m = (l+r)//2
            if arr[m] < x:
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans

    ans = 0
    for i in range(len(arr)):
        a = binarySearch(arr[i]//2, i)
        print(a)
        ans += (i - a)
    return ans


print(solve())
