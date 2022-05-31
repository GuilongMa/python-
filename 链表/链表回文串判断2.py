def reverse(head):
    reverse_head = None
    while head:
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next
    return reverse_head


def huiwei(link_table):
    slow_p = link_table
    fast_p = link_table
    while fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

    reverse_node = reverse(slow_p)
    head_node = link_table
    while head_node and reverse_node:
        if head_node.data == reverse_node.data:
            head_node = head_node.next
            reverse_node = reverse_node.next
        else:
            return False

    return True