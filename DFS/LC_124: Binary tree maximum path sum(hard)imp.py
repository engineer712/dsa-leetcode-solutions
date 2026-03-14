# Approach:
# 1. **Traversal**
#    Use **postorder DFS** (left → right → node) so that the results from left and right children are known before processing the current node.
# 2. **Left and Right Path Values**
#    Recursively compute the maximum path sum from the left and right subtrees.
#    Ignore negative values since they reduce the total sum.
#    left = max(0, dfs(node.left))
#    right = max(0, dfs(node.right))
# 3. **Path Through Current Node**
#    Consider the path where the current node acts as the highest point connecting both subtrees.
#    current = node.val + left + right
#    Update the global maximum if this value is larger.
# 4. **Return Value to Parent**
#    Only one branch can be extended upward to the parent node.
#    return node.val + max(left, right)
# 5. **Global Result**
#    Maintain a global variable storing the maximum path sum found during traversal.
#    After DFS completes, this variable contains the final answer for **Binary Tree Maximum Path Sum**.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):

        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans
