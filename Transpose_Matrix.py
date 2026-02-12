class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        trans = [[0] * row for _ in range(col)]
        for c in range(col):
            for r in range(row):
                trans[c][r] = matrix[r][c]
        return trans
