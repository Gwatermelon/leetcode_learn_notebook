#这道题要想做到时间复杂度平均指令为O(1), 需要使用用空间换取时间的思想，用两个队列，一个队列用于正常的添加数字， 另一个是记录一个递减的数组，这样如果队列删除第一个元素为最大元素时，同步删除递减数组的第一个元素
#一直返回递减数组的第一个元素即可
class MaxQueue:

    def __init__(self):
        self.A, self.B = [] , []


    def max_value(self) -> int:
        if not self.A:
            return -1
        else:
            return self.B[0]

    def push_back(self, value: int) -> None:
        self.A.append(value)

        while self.B and self.B[-1]< value:
            self.B.pop()
       
       
        self.B.append(value)
       

    def pop_front(self) -> int:
        if not self.A:
            return -1
        
        ans= self.A[0]
        if ans == self.B[0]:
            self.B.pop(0)
        del self.A[0]
        return  ans
        



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
