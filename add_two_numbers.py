
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        extra = 0

        n1, n2 = l1, l2
        while n1 and n2:
            v = n1.val + n2.val + extra
            node = ListNode(v % 10)
            extra = v // 10
            cur.next = node
            cur = node

            n1 = n1.next
            n2 = n2.next

        n = n1 or n2
        while n:
            v = n.val + extra
            node = ListNode(v % 10)
            extra = v // 10
            cur.next = node
            cur = node
            n = n.next

        if extra > 0:
            cur.next = ListNode(extra)

        return head.next


def _create(ints):
    head = ListNode(ints[0])
    cur = head
    for i in ints[1:]:
        node = ListNode(i)
        cur.next = node
        cur = node
    return head


def _print(nodes):
    cur = nodes
    while cur:
        print(cur.val, end='')
        cur = cur.next
    print()


if __name__ == "__main__":
    l1 = _create([2, 4, 3])
    l2 = _create([5, 6, 4])
    s = Solution()

    _print(s.addTwoNumbers(l1, l2))
