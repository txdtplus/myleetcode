class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:

        result = []
        if root == None:
            return result       
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                 
        return result[::-1]
    
    def postorderTraversal2(self, root: TreeNode) -> list:

        result = []

        def traversal(root: TreeNode):

            if not root:
                return 
            
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)
        return result

if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    s = Solution()
    print(s.postorderTraversal2(root=t))
