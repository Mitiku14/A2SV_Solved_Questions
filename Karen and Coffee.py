n, k, q = map(int, input().split())
receipes = [0] * (200002)
for _ in range(n):
    a, b = map(int, input().split())
    receipes[a] += 1
    receipes[b + 1] -= 1
pre = [0] * (200002)
for i in range(1, 200002):
    receipes[i] += receipes[i - 1]


for i in range(200002):
    pre[i] = pre[i - 1] 
    if receipes[i] >= k:
        pre[i] += 1
for i in range(q):
    x, y = map(int, input().split())
    print(pre[y] - pre[x -1])


