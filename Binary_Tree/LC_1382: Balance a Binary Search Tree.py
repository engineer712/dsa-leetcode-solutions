#Approach:
# ️ 1. Do inorder traversal → store values in sorted array
# ️ 2. Pick middle value → make it root
# ️ 3. Recursively build left (left half) and right (right half)

class Solution(object):
    def balanceBST(self, root):
        def inorder(root, arr):
            if root is None:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        def arrtobst(arr, low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            root = TreeNode(arr[mid])
            
            root.left = arrtobst(arr, low, mid - 1)
            root.right = arrtobst(arr, mid + 1, high)
            
            return root

        if root is None:
            return None

        arr = []
        inorder(root, arr)

        return arrtobst(arr, 0, len(arr) - 1)
