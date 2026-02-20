
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b = list(map(int,input().split()))
    res= []
    op = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                op += 1
                a[j],a[j+1] = a[j+1],a[j]
                res.append([1,j+1])
    for l in range(len(b)-1):
        for m in range(len(b) - l - 1):
            if b[m] > b[m+1]:
                op += 1
                b[m],b[m+1] = b[m+1],b[m]
                res.append([2,m+1])
    
    for k in range(len(a)):

        if a[k] > b[k]:
            op += 1
            a[k] ,b[k] = b[k], a[k]
            res.append([3,k+1])
    print(op)
    for c,idx in res:
        print(c,idx)
