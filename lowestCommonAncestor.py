# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path2node(root, node, li) -> bool:
            if not root:
                return False
            li.append(root)
            if root.val == node.val:
                return True

            def trans_child(child):
                if child:
                    if path2node(child, node, li):
                        return True
                    else:
                        li.pop()
                        return False
            if trans_child(root.left):
                return True
            return trans_child(root.right)

        p_path = []
        path2node(root, p, p_path)

        q_path = []
        path2node(root, q, q_path)

        pi, qi = 0,0
        PN = len(p_path)
        QN = len(q_path)
        while pi < PN and qi < QN:
            if p_path[pi].val == q_path[qi].val:
                pi += 1
                qi += 1
            else:
                return p_path[pi - 1]
        return p_path[pi - 1]

