class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        i = 0 
        j = len(nums)-1
        res= 0
        while i<j:
            res = max(new_nums[i]+new_nums[j],res)
            i+=1
            j-=1
        return res
