# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#这道题主要是用双指针，更重要的是理解链表的 表示方法。
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former = head
        latter = head
        for i in range(k):
            former = former.next 
        while former is not None :
            former = former.next
            latter = latter.next
        return latter 
