class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(0, len(matrix)) :
            for j in range(0, len(matrix[0])) :
                res[j][i] = matrix[i][j]
        return res