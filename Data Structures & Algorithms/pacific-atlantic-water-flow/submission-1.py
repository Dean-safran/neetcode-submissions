""" pattern is start from destination """ 

"""
Use pacific_reachable set and atlantic_reachable set 

loop across top row, and then loop across left col : 
    DFS from each block, if block not in pacific set, add it

loop across bottom row, and then loop across right col : 
    DFS from each block, if block not in atlantic set, add it

in DFS, RETURN if all neighbors are in a set or are less than curr

loop across entire grid, if block is in both sets, add [r,c] to result 
list
"""

"""
Time : o(rows * cols)
We visit every element in grid twice maximum, 
once if it's pacific reachable, 
and once if it's atlantic reachable, the final loop loops over 
every element in the grid once

Space : o(rows * cols)
Worst case every element in grid is reachable by pacific and atlantic
if it's a mountain with the tip at the center, so each set would store all 
elements in grid
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        moves = [(0,1), (1,0), (0,-1), (-1,0) ]
        rows = len(heights)
        cols = len(heights[0])

        def DFS(r, c, reachable) :
            nonlocal moves, rows, cols

            if (r,c) in reachable :
                return
            
            reachable.add((r,c))
            for dy,dx in moves :
                if ((r + dy) > rows - 1 or
                    (c + dx) > cols - 1 or 
                    min(r + dy, c + dx) < 0) :
                    continue
                if heights[r][c] <= heights[r + dy][c + dx] :
                    DFS(r + dy, c + dx, reachable)
        
        for c in range(cols) :
            DFS(0, c, pacific)
        for r in range(1, rows) :
            DFS(r, 0, pacific)
        for c in range(cols) :
            DFS(rows - 1, c, atlantic)
        for r in range(0, rows - 1) :
            DFS(r, cols - 1, atlantic)

        result = []
        for r in range(rows) :
            for c in range(cols) :
                if (r,c) in pacific and (r,c) in atlantic : 
                    result += [list((r,c))]
        return result
        

        
