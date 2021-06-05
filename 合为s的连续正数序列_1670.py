#比较普通的方法就是滑动窗口， i,j为窗口左右边界， target>  i到j的合就把  左边界i右移一位， taget小于i到j的合就把右边界右移一位， 如果等于，则把两边界的数字添加到结果的列表里，并把左边界右移一位
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i ,j, s ,res = 1,2,3,[]
        while i<j :
            if target == s:
                res.append(list(range(i,j+1)))
            if target <= s:
                s -= i 
                i +=1
            else:
                j+=1
                s+=j
        return res

 #也可以用数学的方法做，因为  target == (i+j-1) *(i+j)/2 ，target和左边界已知（遍历左边界）， 求右边界即可 一元二次方程组 

class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res
#学自K神
