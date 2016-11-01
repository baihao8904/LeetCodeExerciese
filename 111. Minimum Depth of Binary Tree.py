# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = self.findpath(root)
        return path

    def findpath(self,root):
        if root is None:
            return 0
        left = 0
        right=0
        if root.left != None:
            left = self.findpath(root.left)
        else:
            return self.findpath(root.right)+1
        if root.right != None:
            right = self.findpath(root.right)
        else:
            return self.findpath(root.left)+1

        return min(left,right)+1