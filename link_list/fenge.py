# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None:
            return None
        p = ListNode(0)
        p2 = p
        p1 = ListNode(0)
        p3 = p1
        dumpy = head
        while head != None:
            if head.val < x:
                p.next = head
                p = p.next
                head = head.next
            else:
                p1.next = head
                p1 = p1.next
                head = head.next

        if p2.next == None:
            p1.next = None
            return p3.next
        elif p3.next == None:
            return p2.next
        else:

            p.next = p3.next
            p1.next = None
            return p2.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
#    head.next = ListNode(4)
#    head.next.next = ListNode(3)
#    head.next.next.next = ListNode(2)
#    head.next.next.next.next = ListNode(5)
#    head.next.next.next.next.next = ListNode(2)
    x = 0
#    head.next.next.next.next.next.next = ListNode(5)
    aa = solution.partition(head, x)
    print(aa.val,aa.next.val)

