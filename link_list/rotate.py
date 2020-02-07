class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        if not head.next:
            return head
        dd = head
        i = 1
        while dd.next != None:
            dd = dd.next
            i += 1
        dd.next = head
        dd = head
        k = k % i
        for i in range(i-k -1):
            dd = dd.next

        head = dd.next
        dd.next = None


        return head



if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    aa = solution.rotateRight(head, 2)




