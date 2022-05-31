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


    #链表反转
    def revesed(self):
        if self.head is None or len(self) == 1:
            return self
        last = None
        temp = None
        p = self.head
        while p.next is not None:
            temp = p
            p = p.next
            temp.next = last
            last = temp
        p.next = temp
        self.head = p
        return self


if __name__ == "__main__":
    link_table = LinkTable([2,1,3])
    print(link_table)
    link_table.revesed()
    print(link_table)

