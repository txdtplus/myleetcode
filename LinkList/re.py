class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def Reverse(self, head: Node):
        
        if not head:
            return None
        
        cur = head
        pre = None

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        return pre
        


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    s = Solution()
    b = s.Reverse(a)
    print(b)
    print(int(33.15))