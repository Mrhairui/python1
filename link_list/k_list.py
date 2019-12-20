from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists:List[ListNode]) -> ListNode:
        l_list = []
        for list in lists:
            while list:
                l_list.append(list.val)
                list = list.next

        aa = ListNode(0)
        bb = aa
        for t in sorted(l_list):
            aa.next = ListNode(t)
            aa = aa.next

        return bb.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next= ListNode(5)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(8)
    head1 = ListNode(2)
    head1.next = ListNode(7)
    lists = [head, head1]
    solution = Solution()
    pp = solution.mergeKLists(lists)
    print(print(pp.val, pp.next.val, pp.next.next.val, pp.next.next.next.val))


