# LeetCode 104: Maximum Depth of Binary Tree
# Problem: Find the maximum depth (height) of a binary tree.
# Approach: Use DFS recursion to find the depth of left and right subtrees.
# At each node, depth = 1 + max(left_depth, right_depth).



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left,right)

        
