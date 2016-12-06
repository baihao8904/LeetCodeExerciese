# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isbalance,height = self.findNode(root)
        return isbalance


    def findNode(self,root):
        if root is None:
            return True,0
        balance,leftheight = self.findNode(root.left)
        if not balance:
           return False,0
        balance,rightheight = self.findNode(root.right)
        if not balance:
            return False,0

        return abs(leftheight-rightheight)<=1,max(rightheight,leftheight)+1
