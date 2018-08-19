'''
Q872 logic not ocmplete
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

l = []
def get_kids(node):
        #print(node.val)
        if(node.left):
            get_kids(node.left)
            if(node.right):
                get_kids(node.right)
        else:
            l.append(node)
    



ll = []
def get_kids2(node):
        #print(node.val)
        if(node.left):
            get_kids2(node.left)
            if(node.right):
                get_kids2(node.right)
        else:
            ll.append(node)        
class Solution:

            
                
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        get_kids(root1)
        sol = []
        for i in l:
            #print(i.val)
            sol.append(i.val)
        print(sol)
        
        
        get_kids2(root2)
        sol2 = []
        for i in ll:
            #print(i.val)
            sol2.append(i.val)
        print(sol2)
        if(sol == sol2):
            return True
        else:
            return False            
