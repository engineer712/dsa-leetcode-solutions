# **Question:
# Rearrange the linked list so nodes at **odd positions** come first, followed by nodes at "even positions", keeping their order.

# **Approach:

# * Use two pointers: `odd` and `even`.
# * Keep the head of even list (`eveh`).
# * Link odd nodes together and even nodes together while traversing.
# * Attach odd list’s end to even list.
# * Done in-place, O(n) time, O(1) space.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or head.next == None or head.next.next == None:
            return head
        odd = head
        eveh = head.next
        even = head.next
        while even and even.next :
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = eveh
            
        return head
        


        
