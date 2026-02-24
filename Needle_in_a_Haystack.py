from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    cs = Counter(s)
    ct = Counter(t)
    possible = True
    for c in cs:
        if cs[c] > ct[c]:
            possible = False
            break
    if not possible:
        print("Impossible")
        continue
    for c in cs:
        ct[c] -= cs[c]
    remaining = []
    for c in ct:
        remaining.extend([c] * ct[c])
    remaining.sort()
    ans = []
    i = j = 0
    while i < len(s) and j < len(remaining):
        if remaining[j] < s[i]:
            ans.append(remaining[j])
            j += 1
        else:
            ans.append(s[i])
            i += 1
    ans.extend(s[i:])
    ans.extend(remaining[j:])
    print("".join(ans))




