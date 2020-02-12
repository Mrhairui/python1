class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1 = ListNode(-1)
        p3 = p1
        p2 = head
        t = head.val
        if p2.next.val != p2.val:
            p1.next = p2
            p2 = p2.next
            p1 = p1.next
        else:
            p2 = p2.next
        while p2 != None:
            if p2.val == t :
                if p2.next == None:
                    p1.next = None
                    p2 = p2.next
                else:
                    p2 = p2.next
            else:
                if p2.next == None:
                    p1.next = p2
                    p2 = p2.next
                else:
                    t = p2.val
                    if p2.next.val != p2.val:
                        p1.next = p2
                        p2=p2.next
                        p1 = p1.next
                    else:
                        p2 = p2.next
        return p3.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
#    head.next.next.next = ListNode(3)
#    head.next.next.next.next = ListNode(4)
#    head.next.next.next.next.next = ListNode(4)
#    head.next.next.next.next.next.next = ListNode(5)
    aa = solution.deleteDuplicates(head)
    print(aa.val)