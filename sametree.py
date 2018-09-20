# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        '''
        DFS Iterative
        '''
        stack = [(p,q)]
        while(stack):
            node1,node2 = stack.pop()
            
            if not node1 or not node2:
                pass
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                stack.append((node1.left,node2.left))
                stack.append((node1.right,node2.right))
        return True
