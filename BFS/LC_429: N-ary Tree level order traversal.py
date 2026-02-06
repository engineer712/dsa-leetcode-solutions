# usually an N-ary tree is a tree where each node can have any number of children..
# This is a "classic BFS solution" using deque basic
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)

            res.append(level)

        return res
