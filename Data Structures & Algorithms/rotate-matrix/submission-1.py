class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(x, y, matrix) :
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp
            return

        def flip_horiz(x, y, matrix) : 
            height = len(matrix) - 1
            temp = matrix[x][y]
            matrix[x][y] = matrix[height - x][y]
            matrix[height - x][y] = temp
            return

        # flip matrix over horiz axis
        height = len(matrix) 
        width = len(matrix[0])
        for i in range(height // 2) :
            for j in range(width) :
                flip_horiz(i, j, matrix)
        
        # transpose matrix
        for i in range(height) : 
            for j in range(width) : 
                if j >= i :
                    break
                transpose(i, j, matrix)
        return


