# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = None
        p2 = head
        while (p2 is not None):
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1