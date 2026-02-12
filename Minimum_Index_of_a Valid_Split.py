class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        dom = 0
        dominant = max(freq.values()) 
        for key, val in freq.items():
            if val == dominant:
                dom = key
                break
        left  = 0
        right = 0
        for i in range(n):
            if nums[i] == dom:
                left += 1
            right = dominant - left
            if left > (i + 1) // 2 and right > (n - i - 1) // 2:
                return i
        return -1

        
        

        
        
