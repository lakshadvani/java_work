/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
        stack <pair<TreeNode*,TreeNode* >> stk;
        stk.push(pair<TreeNode*,TreeNode*>(p,q));
        while(!stk.empty())
        {
            p = stk.top().first;
            q = stk.top().second;
            if(!p ^ !q || p && q && p->val!=q->val)
                return 0;
            stk.pop();
            if(p&&q)
            {
            stk.push(pair<TreeNode*, TreeNode*> (p->right, q->right));
            stk.push(pair<TreeNode*, TreeNode*> (p->left, q->left));                
            }
        }
    return 1;
    }
};
