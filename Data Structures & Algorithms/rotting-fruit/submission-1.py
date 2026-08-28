from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        use BFS with starting points as rotten fruit

        if a fruit is 1, set it to curr_dist from a rotten 

        if a fruit value is 0 or greater than 1, ignore

        loop through grid, if any fruit is 1, return -1
        otherwise return max value

        """

        dirs = [(0,1), (0,-1), (1,0), (-1,0),]
        max = 0
        q = deque()
        has_fresh = False
        for i in range(len(grid)) :
            for j in range(len(grid[0])) : 
                if grid[i][j] == 1 : 
                    has_fresh = True
                if grid[i][j] == 2 : 
                    q.append((i, j, 0))
        if not has_fresh : 
            return 0
        while q :
            curr_row, curr_col, curr_level = q.popleft()
            if curr_level > max : 
                max = curr_level
            for move in dirs : 
                dy, dx = move
                new_row = curr_row + dy
                new_col = curr_col + dx

                if (new_row < 0 or
                    new_row > len(grid) - 1 or
                    new_col < 0 or 
                    new_col > len(grid[0]) - 1) :
                    continue
                elif grid[new_row][new_col] == 0 :
                    continue
                elif grid[new_row][new_col] == 2 :
                    continue
                elif grid[new_row][new_col] == 1 :
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, curr_level + 1))
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) : 
                if grid[i][j] == 1 : 
                    return -1
        return max