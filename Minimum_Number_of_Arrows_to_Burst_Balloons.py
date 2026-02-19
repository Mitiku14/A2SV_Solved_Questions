class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1])
        first = points[0][1]
        cnt_arrow = 1
        for i in range(1, n):
            if points[i][0] > first:
                cnt_arrow += 1
                first = points[i][1]

        return cnt_arrow
        
            
