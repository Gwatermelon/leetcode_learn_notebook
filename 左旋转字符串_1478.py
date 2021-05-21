#自己随别写的，本质为列表遍历拼接
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        string = list(s)
        tmp_str = []
        for i in range(n):
            tmp_str.append(string[i])
        for i in range(n):
            string.remove (tmp_str[i])
            string.append(tmp_str[i])
        res = ''.join(string)
        return res
#上述方法太啰嗦，简化版如下
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

#由于任何书取余比他大的数都是他本身，例如2取余7是2，所以可以使用取余运算简化上述操作
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)

# 字符串切片
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]
 
