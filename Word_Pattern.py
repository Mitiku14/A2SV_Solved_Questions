class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(word) != len(pattern):
            return False
        
        seen = dict()
        for i in range(len(pattern)):
            if pattern[i] not in seen:
                if word[i] in seen.values():
                    return False
                seen[pattern[i]] = word[i]
            elif seen[pattern[i]] != word[i]:
                return False
        return True
