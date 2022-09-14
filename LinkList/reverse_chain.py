class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def Reverse(self, head: Node):
            
            if head is None:
                return None
            if head.next is None:
                return head
            cur = head
            pre = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
    
            return pre

    def myReverse(self, head: Node):

        if head is None:
            return None
        if head.next is None:
            return head
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def reverseList2(self, head: Node) -> Node:

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
    b = s.reverseList2(a)
    print(b)
    print(int(33.15))