class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1   #a表示 无数字时翻译方式为一种， b表示数字为一时翻译方式为一种
        for i in range(2, len(s) + 1):                                
            
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a
