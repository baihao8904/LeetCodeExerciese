# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        vimhead = ListNode(0)
        vimhead.next = None
        p = vimhead

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1
        else:
            p.next = l2

        return vimhead.next