from tree import TreeNode

class Solution:
    """二叉树层序遍历迭代解法"""

    def levelOrder(self, root: TreeNode) -> list:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results
    
    def levelOrder2(self, root: TreeNode) -> list:
        res = []
        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([]) # start the current depth
            res[depth].append(root.val) # fulfil the current depth
            if  root.left:
                helper(root.left, depth + 1) # process child nodes for the next depth
            if  root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return res

if __name__ == '__main__':
    t = TreeNode(6)
    t.right = TreeNode(7)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(6)
    t.left = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.levelOrder(root=t))