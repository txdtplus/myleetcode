class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:

        result = []

        if root == None:
            return result
        
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return result
    
    def preorderTraversal2(self, root: TreeNode):

        result = []

        def traversal(root: TreeNode):
            if not root:
                return
            
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result

if __name__ == '__main__':
    t = TreeNode(6)
    t.right = TreeNode(7)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(8)
    t.left = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.preorderTraversal(root=t))
