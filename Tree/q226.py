from tree import TreeNode

class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [root]
        results = []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return root

    def invertTree2(self, root:TreeNode) -> TreeNode:
        
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree2(root.left)
        self.invertTree2(root.right)

        return root

    def invertTree3(self, root:TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return root




if __name__ == '__main__':
    t = TreeNode(6)
    t.right = TreeNode(7)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(8)
    t.left = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.invertTree2(root=t))

        
