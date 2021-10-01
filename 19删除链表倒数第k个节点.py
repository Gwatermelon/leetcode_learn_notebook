# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummpy_node =ListNode(1)
        dummpy_node.next = head 
        fast_node = dummpy_node 
        for i in range(n+1):
            fast_node = fast_node.next 
        
        slow_node = dummpy_node 
        while fast_node:
            fast_node=fast_node.next 
            slow_node=slow_node.next 

        slow_node.next =slow_node.next.next 
        return dummpy_node.next 
