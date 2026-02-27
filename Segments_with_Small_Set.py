from collections import defaultdict
n , k = map(int, input().split())
a = list(map(int, input().split()))
freq = defaultdict(int)
l = 0
count = 0
for r in range(n):
    freq[a[r]] += 1
    while len(freq) > k:
        freq[a[l]] -= 1
        
        if freq[a[l]] == 0:
            del freq[a[l]]
        l += 1
    count += (r - l + 1)
print(count)
