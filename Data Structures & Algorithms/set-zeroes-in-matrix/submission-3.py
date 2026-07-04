class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows) :
            for j in range(cols) :
                #if we run into something to process
                if matrix[i][j] == "t" :
                    #mark as processed
                    matrix[i][j] = "p"
                    #check row of 0
                    for row in range(rows) :
                        if (matrix[row][j] == "p" or 
                            matrix[row][j] == "d" or 
                            matrix[row][j] == "t") :
                            continue
                        #to delete later
                        if matrix[row][j] != 0 :
                            matrix[row][j] = "d"
                        #mark need to process
                        elif matrix[row][j] == 0 :
                            matrix[row][j] = "t"
                    for col in range(cols) :
                        if (matrix[i][col] == "p" or 
                            matrix[i][col] == "d" or 
                            matrix[i][col] == "t") :
                            continue
                        #to delete later
                        if matrix[i][col] != 0 :
                            matrix[i][col] = "d"
                        #mark need to process
                        elif matrix[i][col] == 0 :
                            matrix[i][col] = "t"
                elif ( matrix[i][j] == "p" or 
                       matrix[i][j] == "d" or
                       matrix[i][j] != 0 ):
                    continue
                elif matrix[i][j] == 0 :
                    #mark as processed 
                    matrix[i][j] = "p"
                    #check row of 0
                    for row in range(rows) :
                        if (matrix[row][j] == "p" or 
                            matrix[row][j] == "d" or 
                            matrix[row][j] == "t") :
                            continue
                        #to delete later
                        elif matrix[row][j] != 0 :
                            matrix[row][j] = "d"
                        #mark need to process
                        elif matrix[row][j] == 0 :
                            matrix[row][j] = "t"
                    for col in range(cols) :
                        if (matrix[i][col] == "p" or 
                            matrix[i][col] == "d" or 
                            matrix[i][col] == "t") :
                            continue
                        #to delete later
                        elif matrix[i][col] != 0 :
                            matrix[i][col] = "d"
                        #mark need to process
                        elif matrix[i][col] == 0 :
                            matrix[i][col] = "t"
        for i in range(rows) :
            for j in range(cols) :
                if matrix[i][j] == "p" or matrix[i][j] == "d" :
                    matrix[i][j] = 0
        return
    
        