t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))   

    m = int(input())
    blue = list(map(int, input().split()))  
    
    r = [0] * (n + 1)

    for i in range(1, n + 1):
        r[i] = r[i - 1] + red[i - 1]
        
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        b[i] = b[i - 1] + blue[i - 1]
    print(max(r) + max(b))
