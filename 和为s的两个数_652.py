#双指针法，注意的是j是从末尾开始
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i =0
        j = len(nums)-1
        while i <j:
            s = nums[i] +nums[j]
            if s>target:
                j -=1
            elif s < target:
                i+=1
            else :return [nums[i],nums[j]]
                
   
#也可指一遍遍历 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_time ={}
        for index,value in enumerate(nums):
            search_number = target - value 
            if search_number not in dict_time:
                dict_time[value] = index
            else:
                return [search_number,value]
