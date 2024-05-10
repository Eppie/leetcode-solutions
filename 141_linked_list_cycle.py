from common.list_node import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # type: ignore[union-attr]
            if fast == slow:
                return True

        return False
