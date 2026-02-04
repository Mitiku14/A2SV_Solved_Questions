class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            for s, e in ranges:
                if s <= i <= e:
                    break
            else:
                return False
        
        return True
