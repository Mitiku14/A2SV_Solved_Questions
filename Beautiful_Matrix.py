matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
row = len(matrix)
col = len(matrix[0])
for r in range(row):
    for c in range(col):
        if matrix[r][c] == 1:
            print(abs(r -2) + abs(c - 2))


