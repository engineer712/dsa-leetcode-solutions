# Approach:

# * Use **DFS (recursion)** to traverse all root-to-leaf paths.
# * Pass a variable `curr` to track the number formed so far.
# * At each node, update: `curr = curr * 10 + node.val`.
# * If the node is `None`, return `0`.
# * If the node is a **leaf** (no left and right child), return `curr`.
# * Recursively compute left and right subtree sums.
# * Return `left_sum + right_sum`.
# * Start DFS with `curr = 0`.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        curr = 0
        def dfs(root,curr):
            if root == None:
                return 0
            curr = curr* 10 + root.val
            if root.left == None and root.right == None:
                return curr
            left = dfs(root.left,curr)
            right = dfs(root.right,curr)
            return left + right
        
        return dfs(root,curr)
