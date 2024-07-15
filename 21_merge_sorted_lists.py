from common.list_node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """
        Merge two sorted linked lists into one sorted linked list.

        Algorithm:
            - Initialize a dummy pre_head node to help with list merging.
            - Set current to pre_head.
            - Compare the values of nodes from list1 and list2:
                - If list1 node value is less, append it to the merged list.
                - Otherwise, append the list2 node to the merged list.
            - Continue this process until one of the lists is exhausted.
            - Attach the remaining nodes of the non-exhausted list to the merged list.
            - Return the next node of pre_head, which is the actual head of the merged list.

        Example:
            Given two sorted linked lists:
            list1: 1 -> 3 -> 5
            list2: 2 -> 4 -> 6

            Iteration 1:
            - Compare 1 and 2, attach 1 to merged list.
            - Current merged list: 1

            Iteration 2:
            - Compare 3 and 2, attach 2 to merged list.
            - Current merged list: 1 -> 2

            Iteration 3:
            - Compare 3 and 4, attach 3 to merged list.
            - Current merged list: 1 -> 2 -> 3

            Iteration 4:
            - Compare 5 and 4, attach 4 to merged list.
            - Current merged list: 1 -> 2 -> 3 -> 4

            Iteration 5:
            - Compare 5 and 6, attach 5 to merged list.
            - Current merged list: 1 -> 2 -> 3 -> 4 -> 5

            Iteration 6:
            - Attach remaining node 6 to merged list.
            - Final merged list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        """

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
