# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



def dfs(root):
    
    stack = [(root,"")]
    ret = []
    while(stack):
        node,ls = stack.pop()
        if not node.left and not node.right:
            ret.append(ls+str(node.val))
        if node.right:
            stack.append((node.right,ls+str(node.val)))
        if node.left:
            stack.append((node.left,ls+str(node.val)))
    return(ret)


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        print(dfs(root))
