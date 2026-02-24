class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count_boat = 0
        n = len(people)
        people.sort()
        l , r = 0, n - 1
        while l <= r:
            cur = people[l] + people[r]
            if cur <=  limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count_boat += 1
        return count_boat
