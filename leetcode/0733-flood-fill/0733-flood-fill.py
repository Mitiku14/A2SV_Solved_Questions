class Solution:
    def floodFill(self, image, sr, sc, color):
        
        rows = len(image)
        cols = len(image[0])

        start = image[sr][sc]
        if start == color:
            return image

        directions = [
            (-1, 0),  
            (1, 0),   
            (0, -1),  
            (0, 1)    
        ]

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):

            image[r][c] = color

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if inbound(nr, nc) and image[nr][nc] == start:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image