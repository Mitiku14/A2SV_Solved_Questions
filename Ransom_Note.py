class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        rans = Counter(ransomNote)
        if mag == rans:
            return True
        for ch in ransomNote:
            if rans[ch] == mag[ch]:
                continue
            elif rans[ch] > mag[ch]:
                return False
        return True
