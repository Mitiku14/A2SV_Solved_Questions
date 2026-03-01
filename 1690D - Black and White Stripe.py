t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    white = 0
    ans = float('inf')
    l = 0
    for r in range(n):
        if s[r] == 'W':
            white += 1
        while r - l + 1 > k:
            if s[l] == 'W':
                white -= 1
            l += 1
        if r -l + 1 == k:

            ans = min(ans, white)
    print(ans)
