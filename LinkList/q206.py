class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res
        
        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next
            
            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next

    def my_swapPairs(self, head: ListNode) -> ListNode:

            def swap(hd):
                
                if not hd:
                    return None

                if not hd.next:
                    return hd

                pre = hd
                cur = pre.next
                tmp = cur.next

                cur.next = pre
                pre.next = swap(tmp)

                return cur
            
            
            return swap(head)
        


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    s = Solution()
    b = s.swapPairs(a)
    print(b)
    print(int(33.15))