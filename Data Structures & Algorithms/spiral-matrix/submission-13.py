class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        r = len(matrix[0]) 
        btm = len(matrix)
        l = 0
        res = []
        can_travel = True

        while can_travel : 
            # go right 
            if l < r : 
                for i in range(l, r) :
                    res.append(matrix[top][i])
                top += 1
            else : 
                break
            # go down if possible
            if btm > top : 
                for i in range(top, btm) :
                    res.append(matrix[i][r-1])
                r -= 1
            else : 
                break
            # go left if possible
            if l < r : 
                for i in range(r-1, l-1, -1) : 
                    res.append(matrix[btm-1][i])
                btm -= 1
            else : 
                break
            # go up if possible
            if btm > top :
                for i in range(btm-1, top-1, -1) : 
                    res.append(matrix[i][l])
                l += 1
            else : 
                break
        return res
    
        
            