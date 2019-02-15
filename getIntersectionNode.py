# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        refs = set()
        nb = headB
        while nb:
            refs.add(nb)
            nb = nb.next
        
        na = headA
        while na:
            if na in refs:
                return na
            na = na.next

        return None
