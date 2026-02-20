# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.num = k
        
        def inorder(root):
            if not root:
                return None
            
            # Go left
            left = inorder(root.left)
            if left is not None:
                return left
            
            # Process root
            self.num -= 1
            if self.num == 0:
                return root.val
            
            # Go right
            return inorder(root.right)
        
        return inorder(root)
