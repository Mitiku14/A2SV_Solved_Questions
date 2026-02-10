class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        x  = sum([x for x in nums if x % 2 == 0])
        for val, ind in queries:
            if nums[ind] % 2 == 0:
                x -= nums[ind]
            nums[ind] += val
            if nums[ind] % 2 == 0:
                x += nums[ind]
            res.append(x)

        return res
