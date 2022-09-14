# 移除链表元素
from multiprocessing import dummy
from ListNode import ListNode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        dummy_head = ListNode(next=head)
        cur = dummy_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy_head.next

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    s = Solution()
    b = s.removeElements(a, val=3)
    print(b)
    print(int(33.15))

