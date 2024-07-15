import heapq

from common.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        ListNode.__lt__ = lambda self, other: self.val < other.val
        heap: list[ListNode] = []

        for lst in lists:
            if lst:
                heapq.heappush(heap, lst)

        dummy = ListNode()
        current = dummy

        while heap:
            smallest_node = heapq.heappop(heap)

            current.next = smallest_node
            current = current.next

            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)

        return dummy.next
