from linked_lists.singly_linked_list import SinglyLinkedList


def floydsCicleDetectionAlgo(linkedList: SinglyLinkedList):
    slow = linkedList.head
    fast = linkedList.head
    met = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            met = True
            break

    if not met:
        return None

    slow = linkedList.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
