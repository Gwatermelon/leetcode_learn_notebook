# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        queue = [root]
        res = [[root.val]]

        while queue:
            tmp1 =[]
            tmp2 =[]   
            for node in queue:
                 
                if node.left: 
                    tmp1.append(node.left)
                    tmp2.append(node.left.val)
                if node.right: 
                    tmp1.append(node.right)
                    tmp2.append(node.right.val)
            queue = tmp1
            if tmp2:
                res.append(tmp2)
        return res 
   #k神
  class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res

