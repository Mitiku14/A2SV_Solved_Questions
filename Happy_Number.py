class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            res = sum([int(x)**2 for x in str(n)])
            if res in seen:
                return False
            seen.add(res)
            n = res
        return True

        
