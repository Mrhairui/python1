# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        if head == None or head.next == None:
            return head
        while head.next != None:
            if head.val == head.next.val:
                if head.next.next == None:
                    head.next = None
                else:
                    head.next = head.next.next
            else:
                head = head.next

        return p

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
#    head.next.next.next.next.next = ListNode(4)
#    head.next.next.next.next.next.next = ListNode(5)
    aa = solution.deleteDuplicates(head)
    print(aa.val,aa.next.val)