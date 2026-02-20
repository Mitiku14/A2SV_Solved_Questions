class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = []
        for ch in order:
            if ch in cnt:
                res.extend([ch] * cnt[ch])
        for key, val in cnt.items():
            if key not in res:
                res.extend([key] * val)
        return ''.join(res)

