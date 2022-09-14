# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        if not list1:
            return list2
        
        if not list2:
            return list1
            
        num1 = list1.val
        num2 = list2.val

        if num2 > num1:
            head1 = list1
            head2 = list2
        else:
            head1 = list2
            head2 = list1
        
        cur1 = head1
        cur2 = head2
        while cur1.next and cur2:
            
            if cur1.next.val >= cur2.val:
                tmp = cur1.next
                cur1.next = cur2
                cur1 = cur1.next
                cur2 = tmp
            else:
                cur1 = cur1.next
                
        if cur2:
            cur1.next = cur2

        return head1

if __name__ == '__main__':
    # a = ListNode(1)
    # a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # a.next.next.next = ListNode(4)
    # a.next.next.next.next = ListNode(5)
    # a.next.next.next.next.next = ListNode(6)

    # b = ListNode(2)
    # b.next = ListNode(3)
    # b.next.next = ListNode(5)
    # b.next.next.next = ListNode(7)

    a = None
    b = ListNode(0)

    s = Solution()
    b = s.mergeTwoLists(a, b)
    print(b)