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
   
#使用归并排序， 通过测试，但是仍然时间复杂度较高

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def merge_sort(array):
            if len(array) > 1:
                mid = len(array) // 2   #  //是返回整除结果， /是返回浮点数，如 5//2 == 2
                left_half = array[:mid]   #拆分成两个子列表， 最后认为只有一个元素时也是有序的
                right_half = array[mid:]
                merge_sort(left_half)
                merge_sort(right_half)    #到这里认为已经排序好了，下面就是合并两个有序的列表

                i = 0
                j = 0
                k = 0
                while i<len(left_half) and j< len( right_half):
                    if left_half[i] < right_half[j]:
                        array[k] = left_half[i]
                        i = i+1
                    else:
                        array[k] = right_half[j]
                        j = j+1
                    k = k+1
                while i < len(left_half):
                    array[k] = left_half[i]
                    i +=1
                    k +=1
                while j < len(right_half):
                    array[k] = right_half[j]
                    j +=1
                    k +=1     
            return array
        new_arr = merge_sort(arr)
        return(new_arr[0:k])

    
    #快排   
    
    class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            # 子数组长度为 1 时终止递归
            if l >= r: return
            # 哨兵划分操作（以 arr[l] 作为基准数）
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            # 递归左（右）子数组执行哨兵划分
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)
        
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

