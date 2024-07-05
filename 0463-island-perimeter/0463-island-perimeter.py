class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    answer += 4
                    if r > 0 and grid[r-1][c] == 1:
                        answer -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        answer -= 2
        return answer