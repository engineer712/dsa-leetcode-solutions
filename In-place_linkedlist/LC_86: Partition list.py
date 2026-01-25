# Question:
# Given the head of a singly linked list and an integer `x`, partition the list so that all nodes with values **less than `x`** appear before nodes with values **greater than or equal to `x`**.
# The **relative order** of nodes in each partition must be preserved.

# Approach :
# Traverse the linked list once.
# Maintain **two separate lists**:
#   * `small` list for nodes with value `< x`
#   * `high` list for nodes with value `≥ x`
#  Keep track of both **head and tail** pointers.
#  Link nodes to the corresponding list while traversing.
#  After traversal, **attach the small list to the high list**.
#  Return the correct head.
#  Time complexity: **O(n)**
#  Space complexity: **O(1)**
# Simple pointer manipulation, classic linked list pattern 

#Answer:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head or head.next == None:
            return head
        
        sm_h = None
        high_h = None
        temp = head
        high = None
        while temp:
            if temp.val < x:
                if not sm_h:
                    sm_h = temp
                else:
                    small.next = temp
                small = temp
            else:
                if not high_h:
                    high_h = temp  
                else:
                    high.next = temp
                high = temp
            temp = temp.next

        if high:
                high.next = None

        if sm_h :
            small.next = high_h
            return sm_h
        else:
            return high_h
            
        

        
        
        
