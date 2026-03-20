from bisect import bisect_left, bisect_right
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    max_card = a[-1]
    for i in range(n-2):
        for j in range(i + 1, n-1):
            s = a[i] + a[j]

            min_req = max_card - s + 1
            max_allowed = s - 1
            if min_req > max_allowed:
                continue
                
            left_ind = bisect_left(a, min_req, j + 1, n)
            right_ind = bisect_right(a, max_allowed, j + 1, n)
            if right_ind > left_ind:
                ans += (right_ind - left_ind)
    

    print(ans)