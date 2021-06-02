class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B =[],[]


    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:     # >=是为了避免重复最小值被弹出
            self.B.append(x) 

    def pop(self) -> None:
        if self.A.pop() ==self.B[-1]:   #删除A的栈顶元素，并且只有A的栈顶元素为最小值时，才去掉B的栈顶
            self.B.pop()


    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
#使用两个列表完成  时间复杂度为O(1)的实现
