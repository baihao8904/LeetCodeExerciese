# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path = []
        if root is None:
            return path
        self.getPath(root,path,[])
        return path

    def getPath(self,node,path,tmp):
        tmp.append(str(node.val))
        if node.left is None and node.right is None:
            path.append('->'.join(tmp))
            tmp.pop()
            return

        if node.left:
            self.getPath(node.left,path,tmp)
        if node.right:
            self.getPath(node.right,path,tmp)

        tmp.pop()