#自己写的，比较慢的方法。。。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        times={}
        for i in nums:
            if i not in times:
                times[i] =1
            else: times[i] = times[i]+1

        for i in times:
            if times[i] ==1:
                return i
# k神的有限状态自动机

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

