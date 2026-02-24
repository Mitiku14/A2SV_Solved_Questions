class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_occur = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        res = []
        for ind, val in enumerate(s):
            end = max(end, last_occur[val])
            if ind == end:
                res.append(end - start + 1)
                start = end + 1

        return res
