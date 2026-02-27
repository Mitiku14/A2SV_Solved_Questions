n , s = map(int, input().split())
a = list(map(int, input().split()))
max_sum = 0
l = 0
cur_sum = 0
for r in range(n):
    cur_sum += a[r]
    while cur_sum > s:
        cur_sum -= a[l]
        l += 1
    max_sum +=( r - l + 1)
print(max_sum)
