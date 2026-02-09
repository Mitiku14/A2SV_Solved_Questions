class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = []
        sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        res = [v for v, _ in sorted_cnt[:k]]
        return res
