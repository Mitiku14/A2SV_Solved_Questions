class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        letters = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        
        l=[]
        i=0
        ans = []
        def dfs(i):
            nonlocal ans
            nonlocal l
            if i==len(digits):
                ans.append("".join(l))
                return
            for letter in letters[digits[i]]:
                l.append(letter)
                dfs(i+1)
                l.pop(-1)


        dfs(i)
        return ans