class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def my_removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

            if not head:
                return None
            
            if not head.next and n >= 1:
                return None

            dummy = ListNode(next=head)
            slow = dummy
            fast = dummy
            post = slow.next

            for i in range(n):
                fast = fast.next
            
            while fast.next:
                slow = slow.next
                fast = fast.next
                post = slow.next
            
            slow.next = post.next

            return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    s = Solution()
    b = s.my_removeNthFromEnd(a)
    print(b)