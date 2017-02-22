# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        tmp = head

        while p.next is not None:
            if p.next.val == val:
                tmp = tmp.next
                p.next = tmp
            else:
                p = p.next
                tmp = tmp.next

        return head