#这样写时间复杂度太低了
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i % 2 ==1:
                ans.insert(0,i)
            else:
                ans.append(i)
        return ans
#简单的重复两遍反而快了，说明 insert比较耗时    
 class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i %2 ==1:
                ans.append(i)
            else:pass
        for i in nums:
            if i %2 ==1:
                pass
            else:
                ans.append(i)
        return ans
#双指针直接交换左右两边，更快
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left=0
        right = len(nums)-1

        while left <right:
            while left <right and nums[left] % 2 ==1:
                left +=1
            while  left <right and nums[right] % 2 ==0:
                right -=1
            
            nums[left], nums[right] = nums[right] , nums[left]
           
        return nums

