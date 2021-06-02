class Solution:
    def search(self, nums: List[int], target: int) -> int:   #有序的数组查找数首先考虑二分
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i+j) //2
            if nums[mid] <= target:   #这里是小于等于 ，i>j时，  i为右边界
                i =mid+1
            else:
                j = mid -1
        right = i    #找到了 有边界
        i = 0 
        while i <= j:
            mid = (i+j) //2
            if nums[mid] < target:  #这里是小于， 等于在下面else里， i>j时， j为左边界
                i =mid+1
            else:
                j = mid -1
        left = j
        return right -left -1
        
        
        
