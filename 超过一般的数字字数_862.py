#可以用排序，中位数即众数， 也可用字典统计， 也可用摩尔投票法


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count ==0:
                x =i 
            count +=1 if x == i else -1
        return x 
            
