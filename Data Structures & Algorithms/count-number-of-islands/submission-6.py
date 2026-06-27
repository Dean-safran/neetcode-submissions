# init intializes a 2 boards and loops through the board once : 
# o(n) time and space where n = row * col

"""
 anywhere I mentioned log n could be alpha(n) where alpha is 
 the inverse ackerman function, which is nearly amortized constant, hence 
 neetcode's o(row*col) runtime


Union-by-size ensures the trees don't grow too tall,
Path compression flattens them aggressively,
Together, they make the tree depth bounded by something even smaller than 
log n
"""

# find is o(1) space and and o(log n) time (you need to attatch a component
# at least double the size of the current component to increase depth 
# by 1, so finding a root of a component with n nodes could take 
# log n time)
# since we use size comparison in union, with path compression
# the amortized time to look for a root is the inverse ackerman function, 
# which is asympotically smaller than log n by a lot!

# union uses o(1) space and o(log n) time since .find checks are o(log n), 
# size checks are o(1) since indexing into size grid is constant, 
# and adding the sizes of two component roots is constant

# numIslands loops instantiates a UnionFind object, and does 
# one pass over the board doing 2 union operations 
# per block on the board, total time and space is o(n) = o(log n * rows * col)

class UnionFind :
    def __init__(self, board) :
        self.parent = [ [ (r,c) for c in range(len(board[0])) ] for r in range(len(board)) ]
        self.size = [[1 for _ in range(len(board[0])) ] for _ in range(len(board)) ] 
        self.islands = 0
        for row in range(len(board)) :
            for col in range(len(board[0])) :
                if board[row][col] == "1" :
                    self.islands += 1
    
    def find(self, r, c) :
        #find root 
        root_r = r
        root_c = c
        while self.parent[root_r][root_c] != (root_r, root_c) :
            root_r, root_c = self.parent[root_r][root_c]

        #path compress 
        while self.parent[r][c] != (r,c) :
            next_r, next_c = self.parent[r][c]
            self.parent[r][c] = (root_r, root_c)
            r,c = next_r, next_c
        return (root_r, root_c)
        
    #if you're not a root, size won't be read so don't update smaller 
    # root, also only path compress once the block is called, 
    # no need to path compress all nodes in the smaller component 
    # right away
    def union(self, r1, c1, r2, c2) :
        
        if self.find(r1,c1) == self.find(r2, c2) :
            return

        root1_r, root1_c = self.find(r1,c1)
        root2_r, root2_c = self.find(r2,c2)
        if self.size[root1_r][root1_c] >= self.size[root2_r][root2_c]  :
            self.parent[root2_r][root2_c] = (root1_r, root1_c)
            self.size[root1_r][root1_c] += self.size[root2_r][root2_c]
            self.islands -= 1
        else :
            self.parent[root1_r][root1_c] = (root2_r, root2_c)
            self.size[root2_r][root2_c] += self.size[root1_r][root1_c]
            self.islands -= 1
        

        

class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        
        union_find = UnionFind(board)

        for row in range(len(board)) :
            for col in range(len(board[0])) :
                if board[row][col] == "1" :
                    if (row + 1) <= len(board) - 1 and board[row + 1][col] == "1":
                        union_find.union(row, col, row + 1, col)
                    if col + 1 <= len(board[0]) - 1 and board[row][col + 1] == "1" :
                        union_find.union(row, col, row, col + 1)
        return union_find.islands



























"""
space is o(m) for recursion call stack 
where m is the amount of blocks on the grid
spanned by the largest island, so also o(row*col)

time is o(row*col + number of "1" chars on board) = o(row*col)
                                                 ^^^ 
                                        This is because if all the chars
                                        on the board were "1", then we'd
                                        have o(row*col + row*col) = 
                                        o(2*row*col) = o(row*col)


since we do
at least a constant operation (a boolean check for "0" and "#" or a call to 
DFS for "1") on every element in the grid, and DFS visits each "1" once
before turning it into "#"


"""

        # moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # def DFS(r,c) :
            
        #     if (min(r,c) < 0 or 
        #         r >= len(board) or
        #         c >= len(board[0]) or
        #         board[r][c] == "0" or 
        #         board[r][c] == "#") :
        #         return

        #     board[r][c] = "#"
        #     for dy,dx in moves :
        #         DFS(r + dy, c + dx)
        
        # result = 0
        # for row in range(len(board)) :
        #     for col in range(len(board[0])) :
        #         if board[row][col] == "0" or board[row][col] == "#" :
        #             continue
        #         DFS(row, col)
        #         result += 1

        # return result


        # loop over all rows and cols

        # if the starting block is 0 or #(we already visited), 
        # don't recurse

        # foundNeighbor #

        # DFS on all adjacent neighbors, turning them 
        # into # once visited and before 
        # recursing, if you run into 0 or #, return

