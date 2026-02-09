class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = list(s)
        cnt = defaultdict(list)
        res = ""
        for k, v in zip(st, indices):
            cnt[v] = k
        sorted_cnt = sorted(cnt.items(), key=lambda x: x[0])
        for k , v in sorted_cnt:
            res += v
        return res
