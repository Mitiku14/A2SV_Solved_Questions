import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    prev = float('-inf')
    possible = True
    for i in range(n):
        option1 = a[i] 
        idx = bisect.bisect_left(b, prev + a[i])
        option2 = float('inf')
        if idx < m:
            option2 = b[idx] - a[i]
        best = float('inf')
        if option1 >= prev:
            best = min(best, option1)
        if option2 >= prev:
            best = min(best, option2)
        
        if best == float('inf'):
            possible = False
            break
        
        prev = best
    
    print("YES" if possible else "NO")