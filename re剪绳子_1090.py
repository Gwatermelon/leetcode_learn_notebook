class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            return n-1

        if n==4:
            return 4
        sum = 1 
        while n>4 :
            sum *= 3
            n -=3
        return sum*n
