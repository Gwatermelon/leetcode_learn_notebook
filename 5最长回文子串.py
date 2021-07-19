class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.find(s, i, i)       # 以当前字符为中心的最长回文子串
            s2 = self.find(s, i, i+1)     # 以当前字符和下一字符为中心的最长回文子串
            #如果最大长度有变化则更新res
            if max(len(s1), len(s2)) > len(res):
                res = s2 if len(s1) < len(s2) else s1
        return res

    def find(self, s, left, right):
        #找到当前中心的最大长度子串
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
