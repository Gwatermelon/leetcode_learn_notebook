# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        point = head
        ans= []
        while point:
            ans.append(point.val)
            point = point.next
        return ans[::-1]
  
