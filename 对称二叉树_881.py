# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(R,L):
           if not R and not L : return True
           if not L or not R or R.val != L.val: return False

           return recur(R.right, L.left) and recur(L.right,R.left)

        return recur(root.right,root.left) if root else True
