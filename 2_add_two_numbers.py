class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


class Solution:
    @staticmethod
    def node_to_int(node: ListNode | None) -> int:
        if node is None:
            return 0
        n = node.val
        place = 10
        while node.next is not None:
            n += node.next.val * place
            place *= 10
            node = node.next
        return n

    @staticmethod
    def int_to_node(n: int) -> ListNode:
        first_node = ListNode(n % 10)
        current_node = first_node
        n //= 10
        while n > 0:
            current_node.next = ListNode(n % 10)
            current_node = current_node.next
            n //= 10
        return first_node

    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        n1 = self.node_to_int(l1)
        n2 = self.node_to_int(l2)
        return self.int_to_node(n1 + n2)


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    test_output = s.addTwoNumbers(l1, l2)
    assert str(test_output) == str(
        ListNode(7, ListNode(0, ListNode(8)))
    ), f"{test_output}"
