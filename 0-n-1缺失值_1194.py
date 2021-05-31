class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left=0
        right =len(nums)-1
        
        while left<=right:
            mid =(right+left)//2
            if nums[mid]== mid:
                left = mid+1 
            else:
                right =mid-1
            
        return left
      #有序的序列查找第一反应是用二分法，但是细节要注意
