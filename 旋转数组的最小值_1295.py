#自己先写了个构思的版本，主要是就是从数组最右面开始添加数到一个空数组里，最后面的数对于旋转数组来说应该是最大的，倒数第二个数应该减小，以此类推，一旦不满足这个规律，即找到旋转点
#但是这样在整个数组都是旋转数组的时候，是线性查找，例如 3 4 5  就会录乘  543  然后返回3   还是应该考虑二分，更快
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        tmp = []
        for i in numbers[::-1]:
            if not tmp   :
                tmp.append(i) 
            else:

                if tmp[-1]>=i :
                    tmp.append(i)
                 
                else:
                    return tmp[-1]
        if len(tmp) == len(numbers):
            return(tmp[-1])



# k神的二分法


class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]

