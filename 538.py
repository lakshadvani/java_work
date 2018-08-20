# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

l = []
def getlist(root):
    if(root):
        l.append(root.val)
        getlist(root.left)
        getlist(root.right)

def eval(root):
    if(root):
        for i in l: 
            if(int(root.val) < int(i)):
                temp = root.val
                root.val = int(root.val)+int(i)
                print(temp,root.val)
            eval(root.left)
            eval(root.right)

ll = []
def getlist2(root):
    if(root):
        ll.append(root.val)
        getlist2(root.left)
        getlist2(root.right)

        
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        greater tree 
        '''
        global l
        global ll
        getlist(root)
        print(l)
        eval(root)
        getlist2(root)
        return ll

        
            
                    
        
        
