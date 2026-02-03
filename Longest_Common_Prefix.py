class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        common_pre = ""
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                common_pre += first[i]
            else:
                break
        return common_pre
