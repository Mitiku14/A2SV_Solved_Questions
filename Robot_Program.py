import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    res = [0] * (n + 1)
    for i in range(n):
        res[i + 1] = res[i] + (1 if s[i] == 'R' else -1)
    
    first_hit = -1
    for i in range(1, n + 1):
        if x + res[i] == 0:
            first_hit = i
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    ans = 1
    k -= first_hit
    
    cycle = -1
    for i in range(1, n + 1):
        if res[i] == 0:
            cycle = i
            break
    
    if cycle == -1:
        print(ans)
    else:
        ans += k // cycle
        print(ans)
