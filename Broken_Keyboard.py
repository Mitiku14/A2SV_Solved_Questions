t = int(input())
for _ in range(t): 
    s = input()
    n = len(s)
    seen = set()
    i = 0
    while i < n:
        cnt = 1
        while i + 1 < n and s[i] == s[i+ 1]:
            cnt += 1
            i += 1
        if cnt % 2 == 1:
            seen.add(s[i])
        i += 1
    print("".join(sorted(seen)))
