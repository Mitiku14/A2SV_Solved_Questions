import sys
input = sys.stdin.readline
def solve(arr):
    ans = 0
    possible = True

    def dfs(a):
        nonlocal ans, possible

        if len(a) == 1:
            return min(a), max(a)

        mid = len(a) // 2

        lmin, lmax = dfs(a[:mid])
        rmin, rmax = dfs(a[mid:])

        if not possible:
            return 0, 0
        if lmax < rmin:
            return lmin, rmax
        elif rmax < lmin:
            ans += 1
            return rmin, lmax

        else:
            possible = False
            return 0, 0

    dfs(arr)

    return ans if possible else -1
t = int(input())

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))

    print(solve(p))