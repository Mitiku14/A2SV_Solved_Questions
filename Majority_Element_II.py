class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        res = []
        for key, val in cnt.items():
            if val > n//3:
                res.append(key)
        return res
