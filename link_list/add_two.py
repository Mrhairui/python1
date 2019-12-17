class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        b = ListNode(0)
        a = b

        while l1.next != None or l2.next != None:
            if l1.val <= l2.val:
                b.next = l1
                l1 = l1.next
                b = b.next
            else:
                b.next = l2
                l2 = l2.next
                b = b.next

        return a.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next= ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next= ListNode(4)
    solution = Solution()
    pp = solution.mergeTwoLists(l1, l2)
    print(pp.val, pp.next.val, pp.next.next.val, pp.next.next.next.val)

