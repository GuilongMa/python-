def check_circle(link_table):
    slow_p = link_table
    fast_p = link_table
    while fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if fast_p is slow_p:
            return True
    return False