# Approach:
# ️1. Perform **inorder traversal** and store all node values in a list.
# ️2. Check if the list is **strictly increasing** (each value < next value).
# ️3. If any violation is found return `False`, otherwise return `True`. 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        arr = []
        def inorder(root,arr):
            if not root:
                return
            
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        
        inorder(root,arr)
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
