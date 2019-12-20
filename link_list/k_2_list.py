from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head1 = ListNode(2)
    head1.next = ListNode(4)
    solution = Solution()
    pp = solution.merge2Lists(head, head1)
    print(pp.val, pp.next.val, pp.next.next.val, pp.next.next.next.val)