# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxDepth(self, root):
            if root is None:
                return 0
            else:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # if root == None:
        #     return 0
        # length = 0
        # p = root.left
        # q = root.right
        # if p is not None and q is not None:
        #     length+=1
        #     length += max(self.maxDepth(p),self.maxDepth(q))
        # elif p is None and q is not None:
        #     length+=1
        #     length += self.maxDepth(q)
        # elif p is not None and q is None:
        #     length+=1
        #     length += self.maxDepth(p)
        # else:
        #     length+=1
        #
        # return length
