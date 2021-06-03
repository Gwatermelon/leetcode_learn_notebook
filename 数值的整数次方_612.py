#这么写还是太慢了，通不过最后几个测试
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            x=1/x
            for i in range(-n):
                ans =ans* x
        if n > 0:
            for i in range(n):
                ans =ans* x
        if n == 0:
            ans = 1
        return ans
 #根据 k神的解析，这里可以考虑用快速幂法
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n= n//2
            #n >>= 1  n按位右移一位相当于除2
        return res

