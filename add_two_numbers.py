# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = ListNode(None)
        pointer = l3
        sum = 0
        carry = 0

        while (l1.next is not None or l2.next is not None):
            sum = carry
            if l1.next is not None:
                sum += l1.val
                l1 = l1.next

            if l2.next is not None:
                sum += l2.val
                l2 = l2.next

            carry = int(sum/10)
            pointer.next = ListNode(sum%10)
            pointer = pointer.next

        if carry == 1:
            pointer.next = ListNode(carry)

        return l3.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(Solution().addTwoNumbers(l1,l2))