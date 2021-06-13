class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tmp = []
        j = 0
        for i in range(len(pushed)):
            tmp.append(pushed[i])
            while tmp and tmp[-1] ==popped[j]:
                tmp.pop()
                j += 1
       
        if tmp:
            return False
        else:
            return True
