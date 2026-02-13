class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(list)
        for ind, val in enumerate(nums):
            cnt[val].append(ind)
        count = 0
        for ind in cnt.values():
            for ind1, ind2 in combinations(ind, 2):
                if ind1 * ind2 % k == 0:
                    count += 1
        return count
