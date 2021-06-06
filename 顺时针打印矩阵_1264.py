class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left = 0
        right = len(matrix[0])-1
        t = 0
        b=len(matrix)-1
        res = []
        while True:
            for i in range(left,right+1):
                res.append(matrix[t][i])
            t +=1

            if t>b : 
                break

            for i in range(t,b+1):
                res.append(matrix[i][right])
            right -=1
            if left>right:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[b][i])
            b -=1
            if t>b :
                break
            for i in range(b,t-1,-1) :
                res.append(matrix[i][left])
            left +=1
            if left >right :
                break 
        return res  
