# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#自己做出来还是有成就感的。加油
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        top = [root]    
        r_res = []
        r_res.append(root.val)
        while top:
            res=[]
            for node in top:
                if node.left:
                    res.append(node.left)
                    r_res.append(node.left.val)
                if node.right: 
                    res.append(node.right)
                    r_res.append(node.right.val)
                top = res
        
        return r_res
#k神的更简洁

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res

      
