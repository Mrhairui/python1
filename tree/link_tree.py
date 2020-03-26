# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_mid(self, head):
        fast = head
        low = head
        pre = None
        while fast and fast.next :
            pre = low
            fast = fast.next.next
            low = low.next
        if pre:
            pre.next = None
        return low
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        a = self.find_mid(head)
        root = TreeNode(a.val)
        if head == a:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(a.next)
        return root

