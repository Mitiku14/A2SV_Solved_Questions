n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 1
for num in a:
    if num >= cnt:
        cnt += 1
print(cnt - 1)
