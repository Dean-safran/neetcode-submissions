from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        came up with high level alg in 10 minutes
        -> try to implement in 20
        """

        """
        for each land, if not visited, find most optimal 
        treasure chest (the one that's closest)

        make a helper that uses a global min_dist_to_chest
        use bfs to search for nearest chest
        if chest is found and steps(use manhattan dist) to calculate
        is less than min dist, 
        set min dist to curr steps and return 

        set land value to min dist once helper is done
        """

        def helper(row, col, grid) : 
            q = deque()
            q.append((row, col, 0))
            dirs = [(0,1), (0,-1), (1,0), (-1,0),]
            visited = set()
            while q :
                curr_row, curr_col, curr_level = q.popleft() 
                visited.add((curr_row, curr_col))
                for move in dirs : 
                    dy, dx = move
                    new_row = curr_row + dy
                    new_col = curr_col + dx

                    if (new_row < 0 or 
                        new_row > len(grid)-1 or 
                        new_col < 0 or 
                        new_col > len(grid[0])-1) :
                        continue
                    elif grid[new_row][new_col] == 0 :
                        continue
                    elif (new_row, new_col) in visited : 
                        continue
                    elif grid[new_row][new_col] > 0 :
                        if curr_level + 1 < grid[new_row][new_col] :
                            grid[new_row][new_col] = curr_level + 1
                            q.append((new_row, new_col, curr_level + 1))
            return (1<<31) - 1
        
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    helper(i, j, grid)
        
