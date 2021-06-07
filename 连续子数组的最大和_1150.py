
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        temp = 0
        for i in nums:
            temp += i
            if temp > maxSum:
                maxSum = temp 
            if temp < 0:
                temp = 0 
        return maxSum
      
#动态规划如下
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

