"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        result = []
        def check(root,result):
            for i in root.children:
                check(i,result)
                result.append(i)
        check(root,result)

        result.append(root)
        tut = []
        for i in result:
            tut.append(i.val)     
        print(tut)
