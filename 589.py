"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
l = []
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        global l
        if(root):
            l.append(root.val)
            for i in root.children:
                self.preorder(i)
            return(l)
        else:
            return([])
