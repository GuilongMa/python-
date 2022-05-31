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

    def __init__(self, values=None, head=None):
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
            count += 1
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


def maopao_sort(linktable):
    if linktable.head is None:
        return
    temp = linktable.head
    last = None
    while last is not linktable.head.next:
        while temp.next is not last:
            if temp.value > temp.next.value:
                temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next
        last = temp
        temp = linktable.head


# def charu_sort(linktable):
#     temp1 = linktable.head
#     while temp1.next is not None:
#         last = None
#         temp2 = linktable.head
#         while temp2 is not temp1.next:
#             if temp2.value > temp1.next.value:
#                 node = temp1.next
#                 temp1.next = temp1.next.next
#                 node.next = temp2 
#                 if last is None:
#                     last = node
#                 else:
#                     last.next = node
#                 break
#             last = temp2
#             temp2 = temp2.next
#         temp1 = temp1.next


if __name__ == "__main__":
    l1 = LinkTable([2, 3, 1, 5, 8, 7, 6])
    print(l1)
    maopao_sort(l1)
    print(l1)

    # l1 = LinkTable([2,3,1,5,8,7,6])
    # print(l1)
    # charu_sort(l1)
    # print(l1)
