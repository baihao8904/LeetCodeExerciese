# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        resultList = []
        if root is None:
            return resultList
        self.getNode(root,0,resultList)
        return resultList


    def getNode(self,root,level,aList):
        if root is not None:
            if len(aList)<level+1:
                aList.append([])
            aList[level].append(root.val)
            self.getNode(root.left,level+1,aList)
            self.getNode(root.right, level + 1, aList)
