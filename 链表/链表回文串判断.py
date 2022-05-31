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


def check_palindrome(linktable):
    if linktable.head is None:
        return True

    slow = linktable.head
    quick = linktable.head.next
    if quick is None:
        return True
    last = None
    temp = None
    while quick.next is not None:
        quick = quick.next.next
        temp = slow
        slow = slow.next
        temp.next = last
        last = temp

        if quick is None:
            slow_mid = temp
            quick_mid = slow.next
            break
    if quick is not None:
        slow_mid = slow
        quick_mid = slow.next
        slow.next = temp
    while quick_mid and slow_mid:
        if quick_mid.value == slow_mid.value:
            quick_mid = quick_mid.next
            slow_mid = slow_mid.next
            continue
        return False
    return True


if __name__ == "__main__":
    test = LinkTable([1,2,3,2,1])
    print(test)
    print(check_palindrome(test))
    print(check_palindrome(LinkTable([1,2,2,1])))
    print(check_palindrome(LinkTable([1])))
    print(check_palindrome(LinkTable([1,1])))
    print(check_palindrome(LinkTable([1,2])))
    print(check_palindrome(LinkTable()))
    print(check_palindrome(LinkTable([1,2,3,4,2,1])))
