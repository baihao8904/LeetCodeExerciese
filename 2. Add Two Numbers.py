# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head
        carry = 0
        while True:
            if l1 is not None:
                carry +=l1.val
                l1 = l1.next
            if l2 is not None:
                carry +=l2.val
                l2 = l2.next
            ptr.val = carry%10
            carry /=10
            if l1 is not None or l2 is not None or carry!=0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else:
                break
        return head


