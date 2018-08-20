# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
l = {}
def getdepth(root,depth = 0,posn = "center"):
    global l
    if(root):
        l[root.val] = [depth,posn]
        depth = depth+1
        getdepth(root.left,depth,"left")
        getdepth(root.right,depth,"right")
    
    


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        getdepth(root)
        print(l)
        for i in l:
            #print(dir(i))
            print(i.val)
        
        
