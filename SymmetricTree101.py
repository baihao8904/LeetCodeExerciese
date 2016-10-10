# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isequal(root.left,root.right)


    def isequal(self,p,q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isequal(p.left,q.right) and self.isequal(p.right,q.left)
        else:
            return False
