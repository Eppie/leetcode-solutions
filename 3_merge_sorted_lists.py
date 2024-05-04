from common.list_node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        pre_head = ListNode()
        current = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return pre_head.next
