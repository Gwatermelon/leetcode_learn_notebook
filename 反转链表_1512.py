class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prenode = None 
        curnode = head
        while curnode:
            nextnode = curnode.next   #把现在的节点的下一个节点暂时存起来
            curnode.next = prenode   #  现在节点的下一个节点应该变成prenode
            prenode = curnode  #更新prenode
            curnode = nextnode  #最后更新curnode    curnode 一定更新在 prenode后面
        return prenode
      
      
      
