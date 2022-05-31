def reverse(head):
    reverse_head = None
    while head:
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next
    return reverse_head