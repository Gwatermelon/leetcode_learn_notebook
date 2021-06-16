# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#由于 二叉树深度等于左子树深度和右子树深度中的最大值加1,所以可以如下表示，本质为递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#广度优先遍历如下
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        top  =  [root]
        res = 0
        while top:
            tmp = []
            for node in top:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            top = tmp 
            res+=1
        return res
