# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reverse_list(head: ListNode) -> ListNode:

        pre = None
        cur = head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre


##########################################
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
my_sol = Solution()
d = my_sol.reverse_list(l1)
while d:
    print(d.val)
    d = d.next
