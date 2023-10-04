# https://leetcode.com/problems/remove-linked-list-elements/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}]->{self.next}"


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(None, next=head)
    current = head
    prev = dummy
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return dummy.next


def main():
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val = 6
    print(remove_elements(head, val))


if __name__ == '__main__':
    main()
