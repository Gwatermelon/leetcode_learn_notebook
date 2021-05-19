#使用冒泡排序，但是由于时间耗时太长无法完全通过测试用例
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def bubblesort(array):
            for length in range(len(array)-1, 0,-1):  #length为遍历的长度，实际上第一次从0开始比较到末尾，末尾最后一定是最大的数，第二次遍历长度为n-1,因此这里长度第一位为n-1长度，倒叙排列
                for i in range(length):
                    if array[i] >   array[i+1]:
                        tmp = array[i+1]
                        array[i+1] = array[i]
                        array[i] = tmp
            return array
        new_arr = bubblesort(arr)
        return(new_arr[0:k])

# 选择排序，在冒泡排序的基础上减少了交换次数，直接交换最大值和队列最后的元素，但是仍然会测试超时
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def bubblesort(array):
            for length in range(len(array)-1, 0,-1):
                positionmax = 0
                for i in range(1,length+1):                                
                    if array[i] > array[positionmax]:
                        positionmax = i
                    tmp = array[length]
                    array[length] = array[positionmax]
                    array[positionmax] = tmp 
            return array
        new_arr = bubblesort(arr)
        return(new_arr[0:k])
      
 # 插入排序 时间复杂度仍然是n方，还是通不过测试，但是移动操作比交换操作处理时间更少一些

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def insert_sort(array):
            for i in range(1,len(array)):
                current_value = array[i]
                position = i 
                while position>0 and array[position-1]> current_value:
                    array [position] = array[position-1]
                    position = position -1
                array[position] = current_value
            return array
        new_arr = insert_sort(arr)
        return(new_arr[0:k])
