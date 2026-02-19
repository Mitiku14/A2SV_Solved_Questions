class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        if n == 3:
            return piles[1]
        steps = n // 3
        res = 0
        for i in range(2 * steps):
            if i % 2 != 0:
                res += piles[i]
        return res
