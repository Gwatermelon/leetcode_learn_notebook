class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False 
        dp = [0]*len(nums)

        dp[0]= nums[0]
        dp [1] = max(dp[0]-1, nums[1])
        for i in range(2,len(nums)):
            if dp[i-1] <=0:
                return False 
            dp [i] = max(dp[i-1]-1, nums[i])
        if dp[-2]>0:
            return True 
        else:
            return False
