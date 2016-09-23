# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q == None:
            return True
        elif p==None and q !=None:
            return False
        elif p!=None and q==None:
            return False
        if self.Compare(p,q):
            if self.isSameTree(p.left,q.left):
                if self.isSameTree(p.right,q.right):
                    return True
        return False



    def Compare(self,p,q):
        if p.val == q.val:
            return True
        else:
            return False