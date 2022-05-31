class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> [int]:
        rev_head = None
        while head:
            temp = head
            head = head.next
            temp.next = rev_head
            rev_head = temp
        val_list = []
        while rev_head:
            val_list.append(rev_head.val)
            rev_head = rev_head.next
        return val_list

    def reversePrint_2(self, head: ListNode) -> [int]:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        val_list.reverse()
        return val_list

    #递归
    def reversePrint_3(self, head: ListNode) -> [int]:
        if head == None:
            return []
        val_list = self.reversePrint(head.next)
        val_list.append(head.val)
        return val_list


if __name__ == "__main__":
    pass