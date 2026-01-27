# Pattern: DFS + Inorder Traversal
# Inorder == increasing order of BST
# Approach:

# * Perform **inorder traversal** of the tree.
# * Store node values in a list.
# * Check if the list is **strictly increasing**.
# * If any value is greater than or equal to the next, the tree is not a BST.


class Solution(object):
    def isValidBST(self, root):
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True
