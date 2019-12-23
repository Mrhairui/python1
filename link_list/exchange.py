class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp

