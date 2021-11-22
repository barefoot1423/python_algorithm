from typing import Optional

from leetcode.p021_merge_two_sorted_lists.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
        else:
            return ListNode(l2.val, self.mergeTwoLists(l2.next, l1))
