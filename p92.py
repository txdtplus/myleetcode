# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(left-1):
            pre = pre.next
        cur = pre.next
        for i in range(right-left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next




if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)
    a.next.next.next.next.next.next = ListNode(7)


    s = Solution()
    b = s.reverseBetween(a, 2, 5)
    print(b)