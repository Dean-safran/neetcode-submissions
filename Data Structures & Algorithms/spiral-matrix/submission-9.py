class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #todo ->

        # walk through finishing my implementation 
        # and the optimal solution with chatGPT, do 
        # not spend any longer on this problem alone

        START_COL = 0
        START_ROW = 0
        MAX_ROW = len(matrix) - 1
        MAX_COL = len(matrix[0]) - 1
        res = []
        while START_COL <= MAX_COL and START_ROW <= MAX_ROW : 
            for i in range(START_COL, MAX_COL + 1) :
                res.append(matrix[START_ROW][i])
            for i in range(START_ROW + 1, MAX_ROW + 1) :
                res.append(matrix[i][MAX_COL])
            if START_COL <= MAX_COL - 1 and START_ROW <= MAX_ROW - 1 :
                for i in range(MAX_COL - 1, START_COL - 1, -1) :
                    res.append(matrix[MAX_ROW][i])
                for i in range(MAX_ROW - 1, START_ROW, -1) :
                    res.append(matrix[i][START_COL])  
            START_COL += 1
            START_ROW += 1
            MAX_COL -= 1
            MAX_ROW -= 1
        return res   
            