class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0 , int(math.sqrt(c))
        while left <= right:
            cur = left * left + right * right
            if cur > c:
                right -= 1
            elif cur < c:
                left += 1
            else:
                return True
        return False
