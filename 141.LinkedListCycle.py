# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        firstHead = head
        p1 = head
        if firstHead == None:
            return False
        while p1.next is not None and firstHead.next is not None:
            p1 = p1.next
            firstHead = firstHead.next
            if firstHead.next is not None:
                firstHead = firstHead.next
            else:
                return False
            if p1 == firstHead:
                return True

        return False