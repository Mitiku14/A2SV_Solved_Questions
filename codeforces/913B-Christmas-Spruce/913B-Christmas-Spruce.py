n = int(input())

tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    parent = int(input())
    child = i + 2
    tree[parent].append(child)  
for i in range(1, n + 1):
    if len(tree[i])  >  0:
        leaf_children = 0

        for child in tree[i]:
            if len(tree[child]) == 0:
                leaf_children += 1
        
        if leaf_children < 3:
            print("No")
            break
else:
    print("Yes")