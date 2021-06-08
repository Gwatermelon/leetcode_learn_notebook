#用字典的话时间复杂度是O(n)， 没想到K神也说用字典，突如其来的幸福
class Solution:
    def firstUniqChar(self, s: str) -> str:
        s = list(s)
        dict_times={}
        for i in s:
            if i not in dict_times:
                dict_times[i] =1
            else:
                dict_times[i] = dict_times[i]+1
        for i in dict_times:
            if dict_times[i] ==1:
                return i
        
        return " "
            
