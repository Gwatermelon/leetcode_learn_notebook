# 自己随便写的，主要是split自动会把空格去掉
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        ans = ""
        for i in s[::-1]:
            if i != s[0]:
                ans= ans + i+" "
            else: 
                ans =ans +i
        return ans
      
 #当然也可以用join

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s = s[::-1]
        return " ".join(s)
#面试还是考察双指针

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()


        i = j = len(s) -1
        res = []
        while i >=0:
            while i>=0 and s[i] != " ":  #这里我认为要加一个while i>=0 的目的是在i指到最后一个词的第一个字母后，i不再》=0,这时就会跳出 while，append最后一个词，。如果不加，由于最后一个词左边没空格，就会录入不进最后一个词
                i-=1
            res.append(s[i+1:j+1])
            while s[i] == " ":
                i-=1
            j=i
        return " ".join(res)
            
