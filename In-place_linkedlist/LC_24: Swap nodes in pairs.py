# 🔁 LeetCode 24 – Swap Nodes in Pairs

# **Problem:**
# Given a singly linked list, swap every two adjacent nodes and return the modified list.
# You must solve the problem **without modifying node values**—only pointers can be changed.

# **Approach Explanation:**

# * If the list is empty or has only one node, no swap is needed.
# * First, swap the **first two nodes manually** to correctly update the head.
# * Then, traverse the list **pair by pair**.
# * For each pair:

#   * Connect the previous swapped pair to the current pair.
#   * Reverse the current two nodes by adjusting pointers.
# * Move forward by two nodes each time until no pair remains.
# * The algorithm performs all swaps **in-place**, using constant extra space.

# **Time Complexity:** `O(n)`
# **Space Complexity:** `O(1)`



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or head.next == None:
            return head
        curr = head
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = curr
        head = nxt
        
        prev = curr
        curr = curr.next
        if not curr:
            nxt = None
        else: 
            nxt = curr.next
        while nxt != None:
           prev.next = nxt
           curr.next = nxt.next
           nxt.next = curr
           prev = curr
           curr = curr.next
           if not curr:
                nxt = None
           else:
                nxt = curr.next
           
            
        return head
        
        
