# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = head
        cur = head.next 
        if pre.val == val:
            return cur 
        while cur and cur.val != val:
            pre =cur
            cur = cur.next
        if cur:
            pre.next =cur.next 
        return head 
