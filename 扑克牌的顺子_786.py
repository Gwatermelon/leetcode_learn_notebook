class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        while 0 in nums:
            nums.remove(0)
        repeat = set()
        for i in nums:
            if i not in repeat:
                repeat.add(i)
            else:
                return False  
        max_v = max(nums)
        min_v = min(nums)
        
        if max_v-min_v <5:
            return True
        else:
            return False
