class Node(object):

    def __init__(self, value, node=None):
        self.value = value
        self.next = node
    

    def __str__(self):
        return repr(self)


    def __repr__(self):
        return "%s->%s" % (self.value, self.next.value)


class LinkTableUnderflow(ValueError):
    pass

class LinkTable(object):

    def __init__(self, values='', head=None):
        self.head = head
        if not values:
            return
        if isinstance(values, dict):
            values = values.items()
        values = list(values)
        values.reverse()
        for value in values:
            node = Node(value)
            node.next = self.head
            self.head = node

    def __len__(self):
        temp = self.head
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        return count

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            raise LinkTableUnderflow("in pop")
        node = self.head
        self.head = self.head.next
        return node

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def pop_last(self):
        if self.is_empty():
            raise LinkTableUnderflow("in pop_last")
        temp = self.head
        if temp.next is None:
            value = None
            self.head = None
            return value
        while temp.next.next is not None:
            temp = temp.next
        value = temp.next.value
        temp.next = None
        return value

    def __str__(self):
        if self.head is None:
            return []
        List = []
        temp = self.head
        while temp:
            List.append(temp.value)
            temp = temp.next
        return str(List)


def merge_sorted_linktable(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.value <= l2.value:
        l1.next = merge_sorted_linktable(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_linktable(l1, l2.next)
        return l2


if __name__ == "__main__":
    l1 = LinkTable([1,3,5,7])
    print(l1)
    l2 = LinkTable([2,3,9,10])
    print(l2)
    l3 = LinkTable(head=merge_sorted_linktable(l1.head, l2.head))
    print(l3)

