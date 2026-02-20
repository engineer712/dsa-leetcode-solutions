#Approach:
# - The main idea behind this sum is to use reverse inorder traversal(root.right->root->root.left) and to maintain a global variable currsum..

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.currsum = 0
        def dfs(root):
            if root == None:
                return
            dfs(root.right)
            self.currsum += root.val
            root.val  = self.currsum
            dfs(root.left)

        dfs(root)
        return root
