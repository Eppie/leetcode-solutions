from common.list_node import ListNode


class Solution:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: ListNode | None) -> ListNode | None:
        current = head
        while current is not None and current.next is not None:
            g = self.gcd(current.val, current.next.val)
            new_node = ListNode(g, current.next)
            current.next = new_node
            current = new_node.next

        return head
