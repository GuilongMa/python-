class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1 = l1
        temp2 = l2
        while temp1.next or temp2.next:
            if not temp1.next:
                temp1.next = ListNode(0)
            if not temp2.next:
                temp2.next = ListNode(0)
            temp1 = temp1.next
            temp2 = temp2.next

        jin_wei = 0
        res_node = ListNode((l1.val + l2.val + jin_wei) % 10)
        jin_wei = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        last_node = res_node
        while l1 and l2:
            new_node = ListNode((l1.val + l2.val + jin_wei) % 10)
            jin_wei = (l1.val + l2.val + jin_wei) // 10
            l1 = l1.next
            l2 = l2.next
            last_node.next = new_node
            last_node = new_node
        if jin_wei:
            new_node = ListNode(jin_wei)
            last_node.next = new_node
        return res_node


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_node = ListNode(0)
        last_node = res_node
        jin_wei = 0
        temp1 = l1
        temp2 = l2
        while temp1 or temp2:
            if temp1:
                val1 = temp1.val
            else:
                val1 = 0
            if temp2:
                val2 = temp2.val
            else:
                val2 = 0
            sums = val1 + val2 + jin_wei
            new_node = ListNode(sums % 10)
            jin_wei = sums // 10
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
            last_node.next = new_node
            last_node = new_node
        if jin_wei:
            new_node = ListNode(jin_wei)
            last_node.next = new_node
        return res_node.next


if __name__ == "__main__":
    sol = Solution()
    l1_list = [1]
    l2_list = [9, 9]
    l1_node = ListNode(l1_list[0])
    l2_node = ListNode(l2_list[0])
    temp1_node = l1_node
    temp2_node = l2_node
    for i in l1_list[1:]:
        new_node = ListNode(i)
        temp1_node.next = new_node
        temp1_node = temp1_node.next
    for i in l2_list[1:]:
        new_node = ListNode(i)
        temp2_node.next = new_node
        temp2_node = temp2_node.next

    print(l1_node)
    print(l2_node)
    res = sol.addTwoNumbers(l1_node, l2_node)
    print(res)
