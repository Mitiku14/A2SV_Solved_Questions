Divide Players Into Teams of Equal Skill
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        l, r = 0, n - 1
        first = skill[l] + skill[r]
        total = 0
        while l <= r:
            cur = skill[l] + skill[r] 
            if cur == first:
                total += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return total

            
            


        
