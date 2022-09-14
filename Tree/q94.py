from inspect import stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:

        result = []
        stack = []

        cur = root
        while stack or cur:

            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        
        return result

    def inorderTraversal2(self, root: TreeNode) -> list:

        result = []

        def traversal(root: TreeNode):
            if root is None:
                return
            traversal(root=root.left)
            result.append(root.val)
            traversal(root=root.right)
        
        traversal(root)
            
        return result



if __name__ == '__main__':
    t = TreeNode(6)
    t.right = TreeNode(7)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(6)
    t.left = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.inorderTraversal(root=t))
