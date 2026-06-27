#Matrix Exponentiation approach 
"""
The fibonacci sequence can be represented as a matrix operation :

[f(n+1)] = 
 f(n)

[1 1]^n * [f(1)]
 1 0       f(0)

 Since you add the two prev elements in the top row, and 
 use the second element in the bottom row

 We then use Divide and Conquer on the exponentiated matrix
 
 If n is even, we divide with m^(n/2) right away
 If n is odd, we first use m * m^(n-1) and divide 
 m^(n-1) since it's even
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def mult(a,b) :
            return ( [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                     [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]] )
        matrix = [[1,1],[1,0]]
        def recurse(num) :
            nonlocal matrix
            if num == 1 :
                return matrix
            if num % 2 == 0:
                return mult(recurse(num // 2), recurse(num // 2))
            else :
                return mult(matrix, recurse(num - 1))
        expMatrix = recurse(n)
        return expMatrix[1][0] + expMatrix[1][1]





#optimized DP approach

#o(n) time o(1) space

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one = 1
#         two = 1

#         for i in range(2, n + 1) :
#             temp = two
#             new = one + two
#             one = temp
#             two = new
#         return two
