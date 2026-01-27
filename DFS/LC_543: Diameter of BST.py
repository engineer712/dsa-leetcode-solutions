# Question:
# Given the root of a binary tree, return the diameter of the tree.
# The diameter is the length of the longest path between any two nodes,
# measured by the number of edges.

# Core Idea / Approach:
# Use postorder DFS to compute the height of each subtree.
# At every node, the longest path passing through it is:
# height(left subtree) + height(right subtree).
# Track the maximum such value globally while computing heights.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxi = 0

        def height(node):
            if not node:
                return 0
            
            l = height(node.left)
            r = height(node.right)

            self.maxi = max(self.maxi, l + r)
            return 1 + max(l, r)

        height(root)
        return self.maxi
