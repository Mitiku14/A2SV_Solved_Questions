class Solution:    
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        return list(set(a))
