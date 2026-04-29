class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   
        n = len(nums)
        res = []
        def backtrack(ind, cur):
            res.append(cur.copy())
            used = set()
            for i in range(ind, n):
                if nums[i] in used:
                    continue

                used.add(nums[i])

                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])
        return res