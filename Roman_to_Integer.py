class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            'I': 1, 'V' : 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000
        }
        i = 0
        total = 0
        n = len(s)
        while i < n:
            if i == n - 1 or  roman_numbers[s[i]] >= roman_numbers[s[i+1]]:
                total += roman_numbers[s[i]]
                i += 1
            elif roman_numbers[s[i]] <  roman_numbers[s[i+1]]:
                total += (roman_numbers[s[i+1]] - roman_numbers[s[i]])
                i += 2
        return total 
    
