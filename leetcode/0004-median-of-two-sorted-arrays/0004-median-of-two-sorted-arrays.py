class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1, num2 = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(num2) < len(num1):
            num1, num2 = num2, num1  
        left, right = 0, len(num1) - 1
        while True:
            i = (left + right) // 2  
            j = half - i - 2 
            num1left = num1[i] if i >= 0 else float("-infinity")
            num1right = num1[i + 1] if (i + 1) < len(num1) else float("infinity")
            num2left = num2[j] if j >= 0 else float("-infinity")
            num2right = num2[j + 1] if (j + 1) < len(num2) else float("infinity")
            if num1left <= num2right and num2left <= num1right:
                if total % 2: 
                    return min(num1right, num2right)
                return (max(num1left, num2left) + min(num1right, num2right)) / 2  
            elif num1left > num2right:
                right = i - 1
            else:
                left = i + 1






        



