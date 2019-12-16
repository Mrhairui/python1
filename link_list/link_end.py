### 定义链表 ##
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        num = 1
        head_num = head
        while head_num.next != None:
            num = num + 1
            head_num = head_num.next
        res_num = num - n
        cal_head = head
        for i in range(res_num - 1):
            cal_head = cal_head.next
        cal_head.next = cal_head.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    solution = Solution()
    pp = solution.removeNthFromEnd(head, n)
    print(pp.val, pp.next.val, pp.next.next.val, pp.next.next.next.val)







