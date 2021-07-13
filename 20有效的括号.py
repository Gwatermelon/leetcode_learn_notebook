class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}','[':']','(':')','?':'?'}
        res = ['?']
        for i in s:
            if i in dic:
                res.append(i)
            elif dic[res.pop()] != i:         #这里注意的是要pop掉res[-1]，这样的话一旦？ ！= }】）就直接可以返回False,否则只判断res[-1] ！= i的话，会导致res一定为1
                    return False 
        if len(res)==1:
            return True 
        else:
            return False
