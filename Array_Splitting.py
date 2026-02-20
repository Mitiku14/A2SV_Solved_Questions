n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == n:
    print(0)
else:
    total = a[-1] - a[0]
    gaps = []
    for i in range(1, n):
        gaps.append(a[i] - a[i-1])
    gaps.sort(reverse=True)

    for i in range(k-1):
        total -= gaps[i]

    print(total)
