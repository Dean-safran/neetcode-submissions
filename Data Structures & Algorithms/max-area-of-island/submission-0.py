class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        recursively walk through an island, adding 
        visited blocks to a mutable, global visited set 

        keep a global max area variable

        """

        visited = set()
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def helper(row, col, grid) : 
            if (row < 0 or 
                    row > len(grid) - 1 or
                    col < 0 or 
                    col > len(grid[0]) - 1
                ):
                    return 0
            if grid[row][col] == 0 :
                return 0
            if (row, col) in visited :
                return 0
            visited.add((row, col))
            curr_res = 1
            for dy, dx in dirs : 
                next_row = row + dy
                next_col = col + dx
                curr_res += helper(next_row, next_col, grid)
            return curr_res
        
        max = 0
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == 1 and (i, j) not in visited: 
                    curr = helper(i, j, grid)
                    if curr > max :
                        max = curr
        return max