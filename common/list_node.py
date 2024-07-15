from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next_: ListNode | None = None):
        self.val = val
        self.next = next_


# Helper function to convert a list to a linked list.
def list_to_linked_list(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to convert a linked list to a list.
def linked_list_to_list(node: ListNode | None) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
