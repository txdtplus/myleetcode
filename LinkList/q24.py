# 两两交换链表结点
from ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        pre = dummy_head

        while pre.next and pre.next.next:
            cur = pre.next
            post = cur.next

            pre.next = post
            cur.next = post.next
            post.next = cur

            pre = cur
        
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

