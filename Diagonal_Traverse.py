
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        rows = len(mat)
        cols = len(mat[0])

        diagonals = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                diagonals[i + j].append(mat[i][j])
        res = []
        for d in range(rows + cols - 1):
            if d % 2 == 0:
                res.extend(reversed(diagonals[d]))
            else:
                res.extend(diagonals[d])

        return res
