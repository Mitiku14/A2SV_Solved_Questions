from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
max_len = 0
left = 0
right = 0
l = 0
freq = defaultdict(int)

for r in range(n):
    freq[a[r]] += 1
    while len(freq) > k:
        freq[a[l]] -= 1
        if freq[a[l]]  == 0:
            del freq[a[l]]
        l += 1
    if r - l + 1 > max_len:
        max_len = r -l + 1
        left = l
        right = r

print(left + 1, right + 1)

    
