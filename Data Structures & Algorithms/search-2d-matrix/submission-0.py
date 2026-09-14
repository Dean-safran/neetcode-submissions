class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """


        there are m x n entries

        given the ith entry, it is on the (i // row_length)th row, and 
        i - (row_index * row_length) column

        so just binary search with indexes from 0 to m*n - 1, and 
        to access matrix just adjust for the row and col


        """

        def binSearch(l, r, matrix) :
            if r < l :
                return False

            m = (l + r) // 2

            row = m // len(matrix[0])
            col = m - (row * len(matrix[0]))
            
            if target == matrix[row][col] :
                return True
            
            if target > matrix[row][col] :
                return binSearch(m+1, r, matrix)
            
            elif target < matrix[row][col] :
                return binSearch(l, m-1, matrix)
        
        return binSearch(0, ((len(matrix) * len(matrix[0])) - 1), matrix)
