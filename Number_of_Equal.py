from collections import Counter
n , m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
cnt1 = Counter(a)
cnt2 = Counter(b)
for key, val in cnt1.items():
    if key in cnt2:
        tot = val * cnt2[key]
        count += tot

print(count)
