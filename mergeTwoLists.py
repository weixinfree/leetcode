class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        cur = head
        n1, n2 = l1, l2
        while n1 and n2:
            if n1.val <= n2.val:
                node = ListNode(n1.val)
                cur.next = node
                cur = node
                n1 = n1.next
            else:
                node = ListNode(n2.val)
                cur.next = node
                cur = node
                n2 = n2.next

        n = n1 or n2
        if n:
            cur.next = n
        return head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def _create(ints):
    head = ListNode(ints[0])
    cur = head
    for i in ints[1:]:
        node = ListNode(i)
        cur.next = node
        cur = node
    return head


def print_li(li):
    while li:
        print(li.val, end='->')
        li = li.next
    print()


if __name__ == "__main__":
    # print_li(_create([1, 2, 3]))
    s = Solution()
    print_li(s.mergeTwoLists(_create([1, 2, 4]), _create([1, 3, 4])))
