from tree import TreeNode

class Solution:
    def averageofLevels(self, root: TreeNode) -> list:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            levelSum = 0
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                levelSum += cur.val

                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
            
            results.append(levelSum / size)
        
        return results


if __name__ == '__main__':
    t = TreeNode(6)
    t.right = TreeNode(7)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(8)
    t.left = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.averageofLevels(root=t))
